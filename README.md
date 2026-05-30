<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,50:1e3a5f,100:0f4c81&height=200&section=header&text=ClinIQ&fontSize=72&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Clinical%20Decision%20Support%20System&descAlignY=60&descSize=20&descColor=93c5fd"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Ensemble%20ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Multi--page%20UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Persistent%20Storage-003B57?style=flat-square&logo=sqlite&logoColor=white)
![ICD-10](https://img.shields.io/badge/ICD--10-Coded-0ea5e9?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)

**An end-to-end clinical intelligence platform — symptom input to differential diagnosis with triage scoring, ICD-10 codes, SQLite logging, and a real-time analytics dashboard.**

[View Source](https://github.com/aryana-02/Disease-Prediction-Model) · [Report Bug](https://github.com/aryana-02/Disease-Prediction-Model/issues)

</div>

---

## What Is ClinIQ?

ClinIQ is a **full-stack clinical decision support system** built entirely in Python. A clinician (or student) selects symptoms across 11 body systems, and the app returns a ranked differential diagnosis, triage urgency, ICD-10 classification, red flag symptoms, and a persistent prediction history — all inside a polished multi-page Streamlit UI.

This is not a toy notebook. It is a production-style application with a trained ensemble ML model, a relational database layer, and a custom CSS UI — all wired together end to end.

---

## 🛠️ Tech Stack

<div align="center">

<svg width="100%" viewBox="0 0 680 320" role="img" xmlns="http://www.w3.org/2000/svg">
  <title>ClinIQ Tech Stack</title>
  <desc>Four columns showing the tech stack: Language, ML Engine, Frontend, and Database layers</desc>
  <defs>
    <!-- Python logo -->
    <symbol id="py" viewBox="0 0 24 24">
      <path fill="#3776AB" d="M11.9 2C9.1 2 7.4 3.3 7.4 5.2v1.4h4.5v.5H5.6C3.6 7.1 2 8.9 2 11.9s1.4 4.5 3.5 4.9l.5.1v-1.8c0-1.2.7-2 1.9-2h5.7c1 0 1.8-.8 1.8-1.9V5.3C15.4 3.3 13.8 2 11.9 2zm-1.3 1.8c.5 0 .9.4.9.9s-.4.9-.9.9-.9-.4-.9-.9.4-.9.9-.9z"/>
      <path fill="#FFD43B" d="M18.5 7.1h-.5v1.8c0 1.2-.7 2-1.9 2H10.4c-1 0-1.8.8-1.8 1.9v4.9c0 2 1.6 3.2 3.5 3.2 2.8 0 4.5-1.3 4.5-3.2v-1.4H12v-.5h6.3c2 0 3.6-1.8 3.6-4.8s-1.4-4.5-3.4-4.9zm-2.4 9.3c.5 0 .9.4.9.9s-.4.9-.9.9-.9-.4-.9-.9.4-.9.9-.9z"/>
    </symbol>
    <!-- SQL db icon -->
    <symbol id="db" viewBox="0 0 24 24">
      <ellipse cx="12" cy="5" rx="9" ry="3" fill="#003B57"/>
      <path d="M3 5v4c0 1.657 4.03 3 9 3s9-1.343 9-3V5" fill="none" stroke="#003B57" stroke-width="1.5"/>
      <path d="M3 9v4c0 1.657 4.03 3 9 3s9-1.343 9-3V9" fill="none" stroke="#003B57" stroke-width="1.5"/>
      <path d="M3 13v4c0 1.657 4.03 3 9 3s9-1.343 9-3v-4" fill="none" stroke="#003B57" stroke-width="1.5"/>
    </symbol>
    <!-- Streamlit icon simplified -->
    <symbol id="st" viewBox="0 0 24 24">
      <path fill="#FF4B4B" d="M12 2L2 19h20L12 2z"/>
      <path fill="#FF4B4B" d="M5 19L12 8l7 11H5z" opacity="0.6"/>
    </symbol>
  </defs>

  <!-- Column 1: Language -->
  <rect x="40" y="30" width="135" height="260" rx="12" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="0.8"/>
  <rect x="40" y="30" width="135" height="44" rx="12" fill="#3B82F6"/>
  <rect x="40" y="62" width="135" height="12" rx="0" fill="#3B82F6"/>
  <text x="108" y="58" text-anchor="middle" font-family="monospace" font-size="13" font-weight="600" fill="white">Language</text>

  <!-- Python badge -->
  <rect x="60" y="90" width="95" height="32" rx="8" fill="#DBEAFE" stroke="#93C5FD" stroke-width="0.5"/>
  <use href="#py" x="65" y="94" width="20" height="20"/>
  <text x="118" y="111" text-anchor="middle" font-family="monospace" font-size="11" font-weight="600" fill="#1E40AF">Python 3.10+</text>

  <!-- Pandas badge -->
  <rect x="60" y="134" width="95" height="32" rx="8" fill="#DBEAFE" stroke="#93C5FD" stroke-width="0.5"/>
  <rect x="65" y="139" width="20" height="20" rx="3" fill="#150458"/>
  <text x="76" y="154" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="white">pd</text>
  <text x="118" y="155" text-anchor="middle" font-family="monospace" font-size="11" font-weight="600" fill="#1E40AF">Pandas</text>

  <!-- NumPy badge -->
  <rect x="60" y="178" width="95" height="32" rx="8" fill="#DBEAFE" stroke="#93C5FD" stroke-width="0.5"/>
  <rect x="65" y="183" width="20" height="20" rx="3" fill="#013243"/>
  <text x="76" y="198" text-anchor="middle" font-family="monospace" font-size="9" font-weight="700" fill="#4DABCF">np</text>
  <text x="118" y="199" text-anchor="middle" font-family="monospace" font-size="11" font-weight="600" fill="#1E40AF">NumPy</text>

  <!-- Joblib badge -->
  <rect x="60" y="222" width="95" height="32" rx="8" fill="#DBEAFE" stroke="#93C5FD" stroke-width="0.5"/>
  <rect x="65" y="227" width="20" height="20" rx="3" fill="#6366F1"/>
  <text x="76" y="242" text-anchor="middle" font-family="monospace" font-size="8" font-weight="700" fill="white">jbl</text>
  <text x="118" y="242" text-anchor="middle" font-family="monospace" font-size="11" font-weight="600" fill="#1E40AF">Joblib</text>

  <!-- Column 2: ML Engine -->
  <rect x="190" y="30" width="135" height="260" rx="12" fill="#FFF7ED" stroke="#FED7AA" stroke-width="0.8"/>
  <rect x="190" y="30" width="135" height="44" rx="12" fill="#F97316"/>
  <rect x="190" y="62" width="135" height="12" rx="0" fill="#F97316"/>
  <text x="258" y="58" text-anchor="middle" font-family="monospace" font-size="13" font-weight="600" fill="white">ML Engine</text>

  <!-- Sklearn badge -->
  <rect x="210" y="90" width="95" height="32" rx="8" fill="#FFEDD5" stroke="#FED7AA" stroke-width="0.5"/>
  <rect x="215" y="95" width="20" height="20" rx="3" fill="#F97316"/>
  <text x="226" y="110" text-anchor="middle" font-family="monospace" font-size="8" font-weight="700" fill="white">sk</text>
  <text x="268" y="110" text-anchor="middle" font-family="monospace" font-size="10" font-weight="600" fill="#9A3412">Scikit-learn</text>

  <!-- Random Forest badge -->
  <rect x="210" y="134" width="95" height="32" rx="8" fill="#FFEDD5" stroke="#FED7AA" stroke-width="0.5"/>
  <text x="258" y="155" text-anchor="middle" font-family="monospace" font-size="10" font-weight="600" fill="#9A3412">RandomForest</text>

  <!-- GradBoost badge -->
  <rect x="210" y="178" width="95" height="32" rx="8" fill="#FFEDD5" stroke="#FED7AA" stroke-width="0.5"/>
  <text x="258" y="195" text-anchor="middle" font-family="monospace" font-size="9.5" font-weight="600" fill="#9A3412">GradientBoost</text>

  <!-- Voting badge -->
  <rect x="210" y="222" width="95" height="32" rx="8" fill="#FFEDD5" stroke="#FED7AA" stroke-width="0.5"/>
  <text x="258" y="239" text-anchor="middle" font-family="monospace" font-size="9.5" font-weight="600" fill="#9A3412">VotingClassifier</text>

  <!-- Column 3: Frontend -->
  <rect x="340" y="30" width="135" height="260" rx="12" fill="#FFF1F2" stroke="#FECDD3" stroke-width="0.8"/>
  <rect x="340" y="30" width="135" height="44" rx="12" fill="#EF4444"/>
  <rect x="340" y="62" width="135" height="12" rx="0" fill="#EF4444"/>
  <text x="408" y="58" text-anchor="middle" font-family="monospace" font-size="13" font-weight="600" fill="white">Frontend</text>

  <!-- Streamlit badge -->
  <rect x="360" y="90" width="95" height="32" rx="8" fill="#FFE4E6" stroke="#FECDD3" stroke-width="0.5"/>
  <rect x="365" y="95" width="20" height="20" rx="3" fill="#FF4B4B"/>
  <text x="376" y="110" text-anchor="middle" font-family="monospace" font-size="8" font-weight="700" fill="white">ST</text>
  <text x="418" y="110" text-anchor="middle" font-family="monospace" font-size="11" font-weight="600" fill="#9F1239">Streamlit</text>

  <!-- Custom CSS badge -->
  <rect x="360" y="134" width="95" height="32" rx="8" fill="#FFE4E6" stroke="#FECDD3" stroke-width="0.5"/>
  <rect x="365" y="139" width="20" height="20" rx="3" fill="#2563EB"/>
  <text x="376" y="154" text-anchor="middle" font-family="monospace" font-size="8" font-weight="700" fill="white">CSS</text>
  <text x="418" y="155" text-anchor="middle" font-family="monospace" font-size="11" font-weight="600" fill="#9F1239">Custom CSS</text>

  <!-- Google Fonts badge -->
  <rect x="360" y="178" width="95" height="32" rx="8" fill="#FFE4E6" stroke="#FECDD3" stroke-width="0.5"/>
  <rect x="365" y="183" width="20" height="20" rx="10" fill="#4285F4"/>
  <text x="376" y="198" text-anchor="middle" font-family="monospace" font-size="8" font-weight="700" fill="white">G</text>
  <text x="418" y="198" text-anchor="middle" font-family="monospace" font-size="10.5" font-weight="600" fill="#9F1239">Google Fonts</text>

  <!-- 3-page app badge -->
  <rect x="360" y="222" width="95" height="32" rx="8" fill="#FFE4E6" stroke="#FECDD3" stroke-width="0.5"/>
  <text x="408" y="242" text-anchor="middle" font-family="monospace" font-size="10" font-weight="600" fill="#9F1239">3-Page App</text>

  <!-- Column 4: Database -->
  <rect x="490" y="30" width="150" height="260" rx="12" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="0.8"/>
  <rect x="490" y="30" width="150" height="44" rx="12" fill="#16A34A"/>
  <rect x="490" y="62" width="150" height="12" rx="0" fill="#16A34A"/>
  <text x="565" y="58" text-anchor="middle" font-family="monospace" font-size="13" font-weight="600" fill="white">Database</text>

  <!-- SQLite badge -->
  <rect x="510" y="90" width="110" height="32" rx="8" fill="#DCFCE7" stroke="#BBF7D0" stroke-width="0.5"/>
  <rect x="515" y="95" width="20" height="20" rx="3" fill="#003B57"/>
  <text x="526" y="109" text-anchor="middle" font-family="monospace" font-size="7" font-weight="700" fill="white">SQL</text>
  <text x="575" y="110" text-anchor="middle" font-family="monospace" font-size="11" font-weight="600" fill="#14532D">SQLite3</text>

  <!-- Persistent badge -->
  <rect x="510" y="134" width="110" height="32" rx="8" fill="#DCFCE7" stroke="#BBF7D0" stroke-width="0.5"/>
  <text x="565" y="155" text-anchor="middle" font-family="monospace" font-size="10.5" font-weight="600" fill="#14532D">Prediction Log</text>

  <!-- CSV Export badge -->
  <rect x="510" y="178" width="110" height="32" rx="8" fill="#DCFCE7" stroke="#BBF7D0" stroke-width="0.5"/>
  <text x="565" y="199" text-anchor="middle" font-family="monospace" font-size="10.5" font-weight="600" fill="#14532D">CSV Export</text>

  <!-- Analytics badge -->
  <rect x="510" y="222" width="110" height="32" rx="8" fill="#DCFCE7" stroke="#BBF7D0" stroke-width="0.5"/>
  <text x="565" y="242" text-anchor="middle" font-family="monospace" font-size="10.5" font-weight="600" fill="#14532D">Live Analytics</text>
</svg>

</div>

---

## 🏗️ System Architecture

<div align="center">

<svg width="100%" viewBox="0 0 680 520" role="img" xmlns="http://www.w3.org/2000/svg">
  <title>ClinIQ System Architecture</title>
  <desc>Architecture flow from Streamlit UI through ML Engine and Knowledge Base to SQLite database</desc>
  <defs>
    <marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>

  <!-- ── Layer 1: Streamlit UI ─────────────────────────── -->
  <rect x="40" y="20" width="600" height="90" rx="12" fill="#FFF1F2" stroke="#FECDD3" stroke-width="0.8"/>
  <text x="60" y="44" font-family="monospace" font-size="11" font-weight="700" fill="#9F1239">app.py — Streamlit UI (3 pages)</text>

  <!-- Page 1 box -->
  <rect x="60" y="52" width="168" height="44" rx="8" fill="#EF4444" stroke="#FCA5A5" stroke-width="0.5"/>
  <text x="144" y="72" text-anchor="middle" font-family="monospace" font-size="10" font-weight="600" fill="white">🔬 Symptom Assessment</text>
  <text x="144" y="87" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFE4E6">11 categories · 57 symptoms</text>

  <!-- Page 2 box -->
  <rect x="246" y="52" width="168" height="44" rx="8" fill="#EF4444" stroke="#FCA5A5" stroke-width="0.5"/>
  <text x="330" y="72" text-anchor="middle" font-family="monospace" font-size="10" font-weight="600" fill="white">📊 Analytics Dashboard</text>
  <text x="330" y="87" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFE4E6">Triage charts · Top conditions</text>

  <!-- Page 3 box -->
  <rect x="432" y="52" width="168" height="44" rx="8" fill="#EF4444" stroke="#FCA5A5" stroke-width="0.5"/>
  <text x="516" y="72" text-anchor="middle" font-family="monospace" font-size="10" font-weight="600" fill="white">📋 Prediction History</text>
  <text x="516" y="87" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFE4E6">SQL table · CSV export</text>

  <!-- Arrow down from UI to model -->
  <line x1="340" y1="110" x2="340" y2="148" stroke="#94A3B8" stroke-width="1.2" marker-end="url(#arr2)"/>
  <text x="357" y="133" font-family="monospace" font-size="9" fill="#64748B">57-dim vector</text>

  <!-- ── Layer 2: ML Engine ─────────────────────────────── -->
  <rect x="40" y="150" width="600" height="100" rx="12" fill="#FFF7ED" stroke="#FED7AA" stroke-width="0.8"/>
  <text x="60" y="172" font-family="monospace" font-size="11" font-weight="700" fill="#9A3412">model.py — Ensemble ML Engine</text>

  <!-- RF box -->
  <rect x="60" y="182" width="168" height="52" rx="8" fill="#F97316" stroke="#FDBA74" stroke-width="0.5"/>
  <text x="144" y="204" text-anchor="middle" font-family="monospace" font-size="10" font-weight="600" fill="white">RandomForest</text>
  <text x="144" y="220" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFEDD5">200 trees · depth 20</text>
  <text x="144" y="228" text-anchor="middle" font-family="monospace" font-size="8" fill="#FED7AA">weight: 3</text>

  <!-- GB box -->
  <rect x="246" y="182" width="168" height="52" rx="8" fill="#F97316" stroke="#FDBA74" stroke-width="0.5"/>
  <text x="330" y="204" text-anchor="middle" font-family="monospace" font-size="10" font-weight="600" fill="white">GradientBoosting</text>
  <text x="330" y="220" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFEDD5">150 est. · lr 0.08</text>
  <text x="330" y="228" text-anchor="middle" font-family="monospace" font-size="8" fill="#FED7AA">weight: 2</text>

  <!-- Voting box -->
  <rect x="432" y="182" width="168" height="52" rx="8" fill="#EA580C" stroke="#FDBA74" stroke-width="0.5"/>
  <text x="516" y="202" text-anchor="middle" font-family="monospace" font-size="10" font-weight="600" fill="white">VotingClassifier</text>
  <text x="516" y="218" text-anchor="middle" font-family="monospace" font-size="9" fill="#FFEDD5">soft voting · 114 classes</text>
  <text x="516" y="228" text-anchor="middle" font-family="monospace" font-size="8" fill="#FED7AA">→ top-N probabilities</text>

  <!-- Arrow from RF+GB into Voting -->
  <line x1="228" y1="208" x2="430" y2="208" stroke="#94A3B8" stroke-width="0.8" marker-end="url(#arr2)"/>

  <!-- Arrow down from model to knowledge -->
  <line x1="250" y1="250" x2="250" y2="288" stroke="#94A3B8" stroke-width="1.2" marker-end="url(#arr2)"/>
  <text x="267" y="273" font-family="monospace" font-size="9" fill="#64748B">top disease name</text>

  <!-- Arrow down from model to DB -->
  <line x1="470" y1="250" x2="470" y2="378" stroke="#94A3B8" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#arr2)"/>
  <text x="487" y="290" font-family="monospace" font-size="9" fill="#64748B">INSERT prediction</text>

  <!-- ── Layer 3: Knowledge Base ────────────────────────── -->
  <rect x="40" y="290" width="380" height="90" rx="12" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="0.8"/>
  <text x="60" y="312" font-family="monospace" font-size="11" font-weight="700" fill="#1E40AF">disease_info.py — Clinical Knowledge Base</text>

  <rect x="60" y="320" width="100" height="44" rx="8" fill="#3B82F6" stroke="#93C5FD" stroke-width="0.5"/>
  <text x="110" y="340" text-anchor="middle" font-family="monospace" font-size="9" font-weight="600" fill="white">ICD-10</text>
  <text x="110" y="354" text-anchor="middle" font-family="monospace" font-size="8" fill="#DBEAFE">Classification</text>

  <rect x="175" y="320" width="100" height="44" rx="8" fill="#3B82F6" stroke="#93C5FD" stroke-width="0.5"/>
  <text x="225" y="340" text-anchor="middle" font-family="monospace" font-size="9" font-weight="600" fill="white">Triage</text>
  <text x="225" y="354" text-anchor="middle" font-family="monospace" font-size="8" fill="#DBEAFE">4-level urgency</text>

  <rect x="290" y="320" width="110" height="44" rx="8" fill="#3B82F6" stroke="#93C5FD" stroke-width="0.5"/>
  <text x="345" y="338" text-anchor="middle" font-family="monospace" font-size="9" font-weight="600" fill="white">Red Flags &amp;</text>
  <text x="345" y="350" text-anchor="middle" font-family="monospace" font-size="9" font-weight="600" fill="white">Complications</text>

  <!-- ── Layer 4: SQLite ────────────────────────────────── -->
  <rect x="440" y="290" width="200" height="90" rx="12" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="0.8"/>
  <text x="460" y="312" font-family="monospace" font-size="11" font-weight="700" fill="#14532D">database.py — SQLite</text>

  <rect x="460" y="320" width="160" height="44" rx="8" fill="#16A34A" stroke="#86EFAC" stroke-width="0.5"/>
  <text x="540" y="339" text-anchor="middle" font-family="monospace" font-size="9" font-weight="600" fill="white">clinical_predictions.db</text>
  <text x="540" y="354" text-anchor="middle" font-family="monospace" font-size="8" fill="#DCFCE7">session · timestamp · icd10</text>

  <!-- Arrow up from knowledge to UI -->
  <line x1="200" y1="290" x2="200" y2="112" stroke="#94A3B8" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arr2)"/>
  <text x="207" y="200" font-family="monospace" font-size="9" fill="#64748B">clinical profile</text>

  <!-- Arrow up from DB to UI -->
  <line x1="570" y1="290" x2="570" y2="112" stroke="#94A3B8" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arr2)"/>

  <!-- ── Legend ─────────────────────────────────────────── -->
  <line x1="55" y1="415" x2="85" y2="415" stroke="#94A3B8" stroke-width="1.2"/>
  <text x="92" y="419" font-family="monospace" font-size="10" fill="#64748B">data flow</text>
  <line x1="160" y1="415" x2="190" y2="415" stroke="#94A3B8" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="197" y="419" font-family="monospace" font-size="10" fill="#64748B">return path</text>
</svg>

</div>

---

## ✨ Features at a Glance

<div align="center">

<svg width="100%" viewBox="0 0 680 200" role="img" xmlns="http://www.w3.org/2000/svg">
  <title>ClinIQ Features Overview</title>
  <desc>Five feature cards: Ensemble ML, Triage System, ICD-10 Coded, SQLite Persistence, Analytics Dashboard</desc>

  <!-- Card 1: ML -->
  <rect x="20" y="20" width="116" height="160" rx="10" fill="#FFF7ED" stroke="#FED7AA" stroke-width="0.8"/>
  <rect x="20" y="20" width="116" height="44" rx="10" fill="#F97316"/>
  <rect x="20" y="50" width="116" height="14" rx="0" fill="#F97316"/>
  <text x="78" y="48" text-anchor="middle" font-family="monospace" font-size="18" fill="white">🤖</text>
  <text x="78" y="82" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#9A3412">Ensemble ML</text>
  <text x="78" y="98" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#C2410C">RF + GradBoost</text>
  <text x="78" y="112" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#C2410C">VotingClassifier</text>
  <text x="78" y="126" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#C2410C">114 diseases</text>
  <text x="78" y="140" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#C2410C">soft voting</text>
  <text x="78" y="163" text-anchor="middle" font-family="monospace" font-size="8" fill="#EA580C">model.py</text>

  <!-- Card 2: Triage -->
  <rect x="148" y="20" width="116" height="160" rx="10" fill="#FFF1F2" stroke="#FECDD3" stroke-width="0.8"/>
  <rect x="148" y="20" width="116" height="44" rx="10" fill="#EF4444"/>
  <rect x="148" y="50" width="116" height="14" rx="0" fill="#EF4444"/>
  <text x="206" y="48" text-anchor="middle" font-family="monospace" font-size="18" fill="white">🚦</text>
  <text x="206" y="82" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#9F1239">Triage System</text>
  <text x="206" y="98" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#BE123C">🔴 Critical</text>
  <text x="206" y="112" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#BE123C">🟠 Urgent</text>
  <text x="206" y="126" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#BE123C">🟡 Semi-urgent</text>
  <text x="206" y="140" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#BE123C">🟢 Routine</text>
  <text x="206" y="163" text-anchor="middle" font-family="monospace" font-size="8" fill="#E11D48">disease_info.py</text>

  <!-- Card 3: ICD-10 -->
  <rect x="276" y="20" width="116" height="160" rx="10" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="0.8"/>
  <rect x="276" y="20" width="116" height="44" rx="10" fill="#3B82F6"/>
  <rect x="276" y="50" width="116" height="14" rx="0" fill="#3B82F6"/>
  <text x="334" y="48" text-anchor="middle" font-family="monospace" font-size="18" fill="white">🏥</text>
  <text x="334" y="82" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#1E40AF">ICD-10 Coded</text>
  <text x="334" y="98" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#1D4ED8">Medical coding</text>
  <text x="334" y="112" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#1D4ED8">Specialty routing</text>
  <text x="334" y="126" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#1D4ED8">Red flags</text>
  <text x="334" y="140" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#1D4ED8">Complications</text>
  <text x="334" y="163" text-anchor="middle" font-family="monospace" font-size="8" fill="#2563EB">disease_info.py</text>

  <!-- Card 4: SQLite -->
  <rect x="404" y="20" width="116" height="160" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="0.8"/>
  <rect x="404" y="20" width="116" height="44" rx="10" fill="#16A34A"/>
  <rect x="404" y="50" width="116" height="14" rx="0" fill="#16A34A"/>
  <text x="462" y="48" text-anchor="middle" font-family="monospace" font-size="18" fill="white">🗄️</text>
  <text x="462" y="82" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#14532D">Persistence</text>
  <text x="462" y="98" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#166534">SQLite storage</text>
  <text x="462" y="112" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#166534">Session tracking</text>
  <text x="462" y="126" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#166534">Timestamp logs</text>
  <text x="462" y="140" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#166534">CSV export</text>
  <text x="462" y="163" text-anchor="middle" font-family="monospace" font-size="8" fill="#15803D">database.py</text>

  <!-- Card 5: Analytics -->
  <rect x="532" y="20" width="128" height="160" rx="10" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="0.8"/>
  <rect x="532" y="20" width="128" height="44" rx="10" fill="#9333EA"/>
  <rect x="532" y="50" width="128" height="14" rx="0" fill="#9333EA"/>
  <text x="596" y="48" text-anchor="middle" font-family="monospace" font-size="18" fill="white">📊</text>
  <text x="596" y="82" text-anchor="middle" font-family="monospace" font-size="10" font-weight="700" fill="#581C87">Analytics</text>
  <text x="596" y="98" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#6B21A8">Live KPIs</text>
  <text x="596" y="112" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#6B21A8">Top conditions</text>
  <text x="596" y="126" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#6B21A8">Symptom freq.</text>
  <text x="596" y="140" text-anchor="middle" font-family="monospace" font-size="8.5" fill="#6B21A8">Triage chart</text>
  <text x="596" y="163" text-anchor="middle" font-family="monospace" font-size="8" fill="#7C3AED">app.py pg.2</text>
</svg>

</div>

---

## 🔬 ML Model Deep Dive

The model is a **VotingClassifier** combining two estimators with soft probability averaging:

| Estimator | Config | Weight |
|-----------|--------|--------|
| `RandomForestClassifier` | 200 trees, max_depth=20, balanced class weights, n_jobs=-1 | **3** |
| `GradientBoostingClassifier` | 150 estimators, depth=6, lr=0.08, subsample=0.85 | **2** |

`predict_topn()` runs `predict_proba()` on the full 57-dim symptom vector and returns the top-N `(disease, probability%)` pairs sorted by confidence, covering **114 disease classes**.

---

## 🗄️ Database Schema

```sql
CREATE TABLE predictions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id  TEXT,
    timestamp   TEXT,
    symptoms    TEXT,      -- JSON blob of active symptoms + severity
    top1        TEXT,      -- Primary differential
    top2        TEXT,
    top3        TEXT,
    confidence  REAL,      -- Primary prediction confidence (%)
    triage      TEXT,      -- CRITICAL / URGENT / SEMI-URGENT / ROUTINE
    specialty   TEXT,      -- Routing specialty (e.g. Cardiology)
    icd10       TEXT       -- ICD-10 code of primary Dx
);
```

---

## 📁 Project Structure

```
Disease-Prediction-Model/
│
├── app.py               # Streamlit app — 3 pages, custom CSS, full UI logic (299 lines)
├── model.py             # ML engine — ensemble training + predict_topn()  (97 lines)
├── database.py          # SQLite layer — create_tables, insert, query, stats
├── disease_info.py      # Clinical knowledge — ICD-10, triage, red flags, specialties
├── dataset.csv          # Training data — 57 symptoms × 114 diseases
├── model_cache.pkl      # Serialized trained model (auto-generated via joblib)
├── clinical_predictions.db  # SQLite database (auto-generated on first run)
└── requirements.txt     # Python dependencies
```

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/aryana-02/Disease-Prediction-Model.git
cd Disease-Prediction-Model

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

Open `http://localhost:8501`. The model trains on first launch, caches to `model_cache.pkl` — all subsequent loads are instant.

**Dependencies:** `streamlit` · `pandas` · `numpy` · `scikit-learn` · `joblib`

---

## 💼 Skills Demonstrated

<div align="center">

<svg width="100%" viewBox="0 0 680 190" role="img" xmlns="http://www.w3.org/2000/svg">
  <title>Skills Demonstrated by ClinIQ</title>
  <desc>Six skill badges: Ensemble ML, SQL Schema Design, Full-stack Python, Model Serialization, Data Aggregation, UI Engineering</desc>

  <!-- Skill 1 -->
  <rect x="20" y="20" width="200" height="68" rx="10" fill="#FFF7ED" stroke="#FED7AA" stroke-width="0.8"/>
  <rect x="20" y="20" width="6" height="68" rx="3" fill="#F97316"/>
  <text x="38" y="44" font-family="monospace" font-size="11" font-weight="700" fill="#9A3412">Ensemble ML</text>
  <text x="38" y="60" font-family="monospace" font-size="9.5" fill="#C2410C">VotingClassifier with tuned</text>
  <text x="38" y="74" font-family="monospace" font-size="9.5" fill="#C2410C">RF + GradientBoosting</text>

  <!-- Skill 2 -->
  <rect x="240" y="20" width="200" height="68" rx="10" fill="#F0FDF4" stroke="#BBF7D0" stroke-width="0.8"/>
  <rect x="240" y="20" width="6" height="68" rx="3" fill="#16A34A"/>
  <text x="258" y="44" font-family="monospace" font-size="11" font-weight="700" fill="#14532D">SQL Schema Design</text>
  <text x="258" y="60" font-family="monospace" font-size="9.5" fill="#166534">Normalized table, typed cols,</text>
  <text x="258" y="74" font-family="monospace" font-size="9.5" fill="#166534">parameterized queries</text>

  <!-- Skill 3 -->
  <rect x="460" y="20" width="200" height="68" rx="10" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="0.8"/>
  <rect x="460" y="20" width="6" height="68" rx="3" fill="#3B82F6"/>
  <text x="478" y="44" font-family="monospace" font-size="11" font-weight="700" fill="#1E40AF">Full-stack Python</text>
  <text x="478" y="60" font-family="monospace" font-size="9.5" fill="#1D4ED8">UI / Model / DB / Knowledge</text>
  <text x="478" y="74" font-family="monospace" font-size="9.5" fill="#1D4ED8">cleanly separated modules</text>

  <!-- Skill 4 -->
  <rect x="20" y="105" width="200" height="68" rx="10" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="0.8"/>
  <rect x="20" y="105" width="6" height="68" rx="3" fill="#9333EA"/>
  <text x="38" y="129" font-family="monospace" font-size="11" font-weight="700" fill="#581C87">Model Serialization</text>
  <text x="38" y="145" font-family="monospace" font-size="9.5" fill="#6B21A8">joblib cache + force-retrain</text>
  <text x="38" y="159" font-family="monospace" font-size="9.5" fill="#6B21A8">flag pattern</text>

  <!-- Skill 5 -->
  <rect x="240" y="105" width="200" height="68" rx="10" fill="#FFF1F2" stroke="#FECDD3" stroke-width="0.8"/>
  <rect x="240" y="105" width="6" height="68" rx="3" fill="#EF4444"/>
  <text x="258" y="129" font-family="monospace" font-size="11" font-weight="700" fill="#9F1239">Data Aggregation</text>
  <text x="258" y="145" font-family="monospace" font-size="9.5" fill="#BE123C">GROUP BY, COUNT, multi-</text>
  <text x="258" y="159" font-family="monospace" font-size="9.5" fill="#BE123C">table SQL analytics queries</text>

  <!-- Skill 6 -->
  <rect x="460" y="105" width="200" height="68" rx="10" fill="#FEFCE8" stroke="#FEF08A" stroke-width="0.8"/>
  <rect x="460" y="105" width="6" height="68" rx="3" fill="#CA8A04"/>
  <text x="478" y="129" font-family="monospace" font-size="11" font-weight="700" fill="#713F12">UI Engineering</text>
  <text x="478" y="145" font-family="monospace" font-size="9.5" fill="#854D0E">Custom CSS, Google Fonts,</text>
  <text x="478" y="159" font-family="monospace" font-size="9.5" fill="#854D0E">3-page Streamlit layout</text>
</svg>

</div>

---

## ⚠️ Disclaimer

> ClinIQ is built for **educational and portfolio purposes only**. It is not a licensed medical device and should never replace a qualified clinician. All predictions are probabilistic and require clinical validation.

---

## 👩‍💻 Author

**Aryana Sharma** — B.Tech CSE (Health Informatics), VIT Bhopal

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aryana-sharma-284141407)
[![GitHub](https://img.shields.io/badge/GitHub-aryana--02-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aryana-02)

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f4c81,50:1e3a5f,100:0f172a&height=100&section=footer"/>
</div>
