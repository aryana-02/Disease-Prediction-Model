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

### 🛠️ Tech Stack

**Language**
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)

**ML Engine**
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![Random Forest](https://img.shields.io/badge/Random_Forest-228B22)
![Gradient Boosting](https://img.shields.io/badge/Gradient_Boosting-FF9800)

**Frontend**
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

**Database**
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
## 🏗️ System Architecture

```mermaid
flowchart TD
    UI[Streamlit UI<br/>3 Pages]

    UI --> SA[Symptom Assessment]
    UI --> AD[Analytics Dashboard]
    UI --> PH[Prediction History]

    SA --> ML[Ensemble ML Engine]

    ML --> RF[Random Forest]
    ML --> GB[Gradient Boosting]

    RF --> VC[Voting Classifier]
    GB --> VC

    VC --> KB[Clinical Knowledge Base]
    VC --> DB[(SQLite Database)]

    KB --> ICD[ICD-10]
    KB --> TRIAGE[Triage Levels]
    KB --> FLAGS[Red Flags]

    DB --> PH
    KB --> UI
```
## ✨ Features at a Glance

| 🤖 Ensemble ML | 🚦 Triage System | 🏥 ICD-10 Coded |
|---------------|------------------|----------------|
| RF + GradientBoosting | 4-level urgency classification | Medical coding support |
| VotingClassifier | Critical → Routine | Specialty routing |
| 114 disease classes | Clinical prioritization | Red flags & complications |

| 🗄️ Persistence | 📊 Analytics Dashboard |
|---------------|----------------------|
| SQLite storage | Live KPIs |
| Session tracking | Top conditions |
| Timestamp logs | Symptom frequency |
| CSV export | Triage visualizations |

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

> [!TIP]
> **🧠 Ensemble ML**  
> VotingClassifier with tuned Random Forest and Gradient Boosting models.

> [!NOTE]
> **🗄️ SQL Schema Design**  
> Normalized tables, typed columns, and parameterized queries.

> [!IMPORTANT]
> **🐍 Full-Stack Python**  
> Separation of UI, model, database, and knowledge modules.

> [!TIP]
> **📦 Model Serialization**  
> Joblib caching with force-retrain workflow.

> [!NOTE]
> **📊 Data Aggregation**  
> GROUP BY, COUNT, and analytics queries using SQLite.

> [!IMPORTANT]
> **🎨 UI Engineering**  
> Custom CSS, Google Fonts, and a multi-page Streamlit interface.

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
