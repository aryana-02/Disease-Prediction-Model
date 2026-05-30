import streamlit as st
import pandas as pd
import numpy as np
import json
import uuid
from datetime import datetime

from model import train_model, predict_topn, SYMPTOMS, SYMPTOM_CATEGORIES
from database import create_tables, insert_prediction, get_all_predictions, get_stats
from disease_info import disease_details, TRIAGE, SPECIALTY_ICONS

# ─── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ClinIQ — Clinical Decision Support",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1, h2, h3 { font-family: 'DM Serif Display', serif; }

.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2.6rem;
    color: #0f172a;
    line-height: 1.1;
    margin-bottom: 0.2rem;
}
.hero-sub {
    color: #64748b;
    font-size: 1rem;
    margin-bottom: 1.5rem;
}
.triage-banner {
    border-radius: 10px;
    padding: 14px 20px;
    font-weight: 600;
    font-size: 1.05rem;
    margin-bottom: 12px;
    border-left: 5px solid;
}
.diff-card {
    border-radius: 8px;
    padding: 12px 16px;
    margin: 6px 0;
    border: 1px solid #e2e8f0;
    background: #f8fafc;
}
.badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-right: 4px;
}
.redFlag {
    background: #fee2e2;
    color: #991b1b;
    border-radius: 6px;
    padding: 4px 10px;
    margin: 4px 2px;
    font-size: 0.85rem;
    display: inline-block;
}
.stSlider > div > div > div > div { background: #2563eb !important; }
</style>
""", unsafe_allow_html=True)

# ─── Init ─────────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner="Training ensemble model…")
def load_model():
    return train_model()

create_tables()
model = load_model()

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🩺 ClinIQ")
    st.caption("Clinical Decision Support System")
    st.divider()
    page = st.radio("Navigate", ["🔬 Symptom Assessment", "📊 Analytics Dashboard", "📋 Prediction History"])
    st.divider()
    st.markdown(f"**Session:** `{st.session_state.session_id}`")
    st.caption("⚠️ For educational purposes only. Not a substitute for medical advice.")

# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE 1 — SYMPTOM ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════════════
if page == "🔬 Symptom Assessment":
    st.markdown('<div class="hero-title">🩺 ClinIQ Clinical Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Multi-system differential diagnosis · 114 conditions · Ensemble ML</div>', unsafe_allow_html=True)

    st.info("Rate each symptom: **0** = Absent  |  **1** = Mild  |  **2** = Severe", icon="ℹ️")

    symptom_values = {}

    for category, syms in SYMPTOM_CATEGORIES.items():
        with st.expander(f"**{category}**", expanded=(category == "General / Constitutional")):
            cols = st.columns(2)
            for i, sym in enumerate(syms):
                label = sym.replace("_", " ").title()
                val = cols[i % 2].select_slider(
                    label,
                    options=[0, 1, 2],
                    value=0,
                    format_func=lambda x: ["○ None", "◑ Mild", "● Severe"][x],
                    key=f"sym_{sym}"
                )
                symptom_values[sym] = val

    # Fill remaining symptoms not in categories
    for sym in SYMPTOMS:
        if sym not in symptom_values:
            symptom_values[sym] = 0

    st.divider()
    col_btn1, col_btn2 = st.columns([1, 4])
    run = col_btn1.button("🔍 Analyse", type="primary", use_container_width=True)
    col_btn2.button("↺ Reset", on_click=lambda: st.session_state.update({f"sym_{s}": 0 for s in SYMPTOMS}))

    if run:
        active_count = sum(1 for v in symptom_values.values() if v > 0)
        if active_count == 0:
            st.warning("Please select at least one symptom before analysing.")
            st.stop()

        vector = [symptom_values[s] for s in SYMPTOMS]
        top5   = predict_topn(model, vector, n=5)

        top_disease, top_conf = top5[0]
        info = disease_details.get(top_disease, {})
        triage_key = info.get("triage", "ROUTINE")
        triage_info = TRIAGE[triage_key]
        specialty   = info.get("specialty", "General Practice")
        icd10       = info.get("icd10", "—")
        spec_icon   = SPECIALTY_ICONS.get(specialty.split("/")[0].strip(), "🏥")

        # Persist
        insert_prediction(
            {s: v for s, v in symptom_values.items() if v > 0},
            top5, triage_key, specialty, icd10,
            st.session_state.session_id
        )

        # ── Triage Banner ──
        st.markdown(
            f'<div class="triage-banner" style="background:{triage_info["color"]}18;'
            f'border-color:{triage_info["color"]};color:{triage_info["color"]}">'
            f'{triage_info["label"]} &nbsp;—&nbsp; {triage_info["action"]}</div>',
            unsafe_allow_html=True
        )

        # ── Primary result ──
        c1, c2, c3, c4 = st.columns([3, 1.5, 1.5, 1.5])
        c1.metric("Primary Differential", top_disease)
        c2.metric("Confidence", f"{top_conf:.1f}%")
        c3.metric("Specialty", f"{spec_icon} {specialty.split('/')[0].strip()}")
        c4.metric("ICD-10", icd10)

        # ── Confidence bar ──
        st.progress(int(top_conf), text=f"Model confidence: {top_conf:.1f}%")

        if top_conf < 55:
            st.warning("⚠️ Low confidence — symptom profile may span multiple conditions. Broaden differential.")

        # ── Differential Diagnosis table ──
        st.markdown("#### 📋 Differential Diagnosis")
        diff_cols = st.columns([4, 1, 2, 2])
        diff_cols[0].markdown("**Condition**")
        diff_cols[1].markdown("**Prob.**")
        diff_cols[2].markdown("**Triage**")
        diff_cols[3].markdown("**Specialty**")
        for rank, (dis, prob) in enumerate(top5):
            inf = disease_details.get(dis, {})
            t   = TRIAGE.get(inf.get("triage", "ROUTINE"), TRIAGE["ROUTINE"])
            sp  = inf.get("specialty", "General Practice").split("/")[0].strip()
            ic  = inf.get("icd10", "—")
            cols = st.columns([4, 1, 2, 2])
            prefix = "▶ " if rank == 0 else f"{rank+1}. "
            cols[0].markdown(f"**{prefix}{dis}** &nbsp; `{ic}`")
            bar_w = int(prob / top5[0][1] * 100) if top5[0][1] > 0 else 0
            cols[1].markdown(f"`{prob:.1f}%`")
            cols[2].markdown(f'<span style="color:{t["color"]}">{t["label"].split("—")[0].strip()}</span>', unsafe_allow_html=True)
            cols[3].markdown(f"{SPECIALTY_ICONS.get(sp, '🏥')} {sp}")

        st.divider()

        # ── Clinical Detail (primary) ──
        if info:
            st.markdown(f"### 🔬 Clinical Profile — {top_disease}")
            d1, d2 = st.columns(2)

            with d1:
                st.markdown("**Clinical Advice**")
                st.info(info.get("advice", "—"))
                st.markdown("**Prevalence**")
                st.write(info.get("prevalence", "—"))
                contagious_label = "✅ Contagious" if info.get("contagious") else "🚫 Not Contagious"
                st.write(contagious_label)

            with d2:
                if info.get("red_flags"):
                    st.markdown("**🚩 Red Flag Symptoms**")
                    flags_html = " ".join(f'<span class="redFlag">⚑ {f}</span>' for f in info["red_flags"])
                    st.markdown(flags_html, unsafe_allow_html=True)

                if info.get("complications"):
                    st.markdown("**⚠️ Potential Complications**")
                    st.write(" · ".join(info["complications"]))

        st.error("🚨 ClinIQ is an educational AI tool, not a licensed medical device. Always consult a qualified clinician.")


# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE 2 — ANALYTICS DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "📊 Analytics Dashboard":
    st.markdown("## 📊 Population Analytics")
    stats = get_stats()

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Assessments", stats["total"])

    triage_counts = {r["triage"]: r["cnt"] for r in stats["by_triage"]}
    m2.metric("Critical Flags", triage_counts.get("CRITICAL", 0), delta_color="inverse")
    m3.metric("Urgent Cases", triage_counts.get("URGENT", 0))
    m4.metric("Unique Conditions", len(stats["by_disease"]))

    st.divider()

    col_l, col_r = st.columns(2)

    with col_l:
        st.markdown("#### 🏆 Top Predicted Conditions")
        if stats["by_disease"]:
            df_dis = pd.DataFrame(stats["by_disease"]).rename(columns={"top1": "Condition", "cnt": "Count"})
            st.dataframe(df_dis, use_container_width=True, hide_index=True)
        else:
            st.info("No data yet. Run some assessments first.")

    with col_r:
        st.markdown("#### 🔬 Most Reported Symptoms")
        if stats["top_symptoms"]:
            df_sym = pd.DataFrame(stats["top_symptoms"]).rename(
                columns={"symptom": "Symptom", "total_count": "Reports"}
            )
            df_sym["Symptom"] = df_sym["Symptom"].str.replace("_", " ").str.title()
            st.dataframe(df_sym, use_container_width=True, hide_index=True)
        else:
            st.info("No data yet.")

    st.divider()
    st.markdown("#### 🚦 Triage Distribution")
    if stats["by_triage"]:
        df_t = pd.DataFrame(stats["by_triage"]).rename(columns={"triage": "Level", "cnt": "Count"})
        st.bar_chart(df_t.set_index("Level"))


# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE 3 — PREDICTION HISTORY
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "📋 Prediction History":
    st.markdown("## 📋 Prediction History")
    records = get_all_predictions(limit=100)

    if not records:
        st.info("No predictions yet. Run an assessment to begin.")
    else:
        df = pd.DataFrame(records)
        df["timestamp"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d %H:%M")
        df["confidence"] = df["confidence"].round(1).astype(str) + "%"
        display_cols = ["timestamp", "top1", "top2", "top3", "confidence", "triage", "specialty", "icd10"]
        st.dataframe(
            df[display_cols].rename(columns={
                "timestamp": "Time", "top1": "Primary Dx", "top2": "2nd Dx",
                "top3": "3rd Dx", "confidence": "Confidence",
                "triage": "Triage", "specialty": "Specialty", "icd10": "ICD-10"
            }),
            use_container_width=True,
            hide_index=True,
        )

        st.download_button(
            "⬇ Export CSV",
            df[display_cols].to_csv(index=False).encode(),
            file_name=f"cliniq_history_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
