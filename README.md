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

ClinIQ is a **full-stack clinical decision support system** built entirely in Python. A clinician (or student) selects symptoms across 11 body systems, and the app returns:

- A **ranked differential diagnosis** (top 5 conditions with confidence scores)
- **Triage urgency** — CRITICAL / URGENT / SEMI-URGENT / ROUTINE
- **ICD-10 classification** and medical specialty routing
- **Red flag symptoms** and potential complications for the primary diagnosis
- **Persistent prediction history** logged to SQLite, exportable as CSV
- A live **population analytics dashboard** across all sessions

This is not a toy notebook. It is a multi-page Streamlit application with a trained ensemble ML model, a relational database layer, and a custom CSS UI — all wired together production-style.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        app.py  (Streamlit UI)                   │
│  ┌─────────────────┐  ┌──────────────────┐  ┌───────────────┐  │
│  │ Symptom          │  │ Analytics         │  │ Prediction    │  │
│  │ Assessment       │  │ Dashboard         │  │ History       │  │
│  │ (11 categories)  │  │ (triage charts,   │  │ (SQL table,   │  │
│  │                  │  │  top conditions)  │  │  CSV export)  │  │
│  └────────┬─────────┘  └──────────────────┘  └───────────────┘  │
└───────────┼─────────────────────────────────────────────────────┘
            │ symptom vector [0,1,2] × 57 features
            ▼
┌─────────────────────────────────────────────────────────────────┐
│                        model.py  (ML Engine)                    │
│                                                                 │
│   RandomForest (200 trees)  ──┐                                 │
│   GradientBoosting (150)    ──┴──► VotingClassifier (soft)      │
│                                    weights [3, 2]               │
│                                    → top-N probabilities        │
│                                    → 114 disease classes        │
└───────────────────────────────────────────────────────────────-─┘
            │
            ▼
┌─────────────────────────────────────────────────────────────────┐
│              disease_info.py  (Clinical Knowledge Base)         │
│   ICD-10 codes · Triage levels · Red flags · Complications      │
│   Specialty routing · Contagion flags · Prevalence data         │
└─────────────────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  database.py  (SQLite Persistence)              │
│   Table: predictions                                            │
│   Columns: session_id, timestamp, symptoms_json, top1–top5,     │
│            confidence, triage, specialty, icd10                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Features

### 🔬 Symptom Assessment Engine
- **57 clinical symptoms** across 11 body-system categories (General, Respiratory, Cardiovascular, GI, Neurological, Musculoskeletal, Dermatological, Urological, ENT, Haematological, Endocrine)
- Severity scoring per symptom: `0 = Absent | 1 = Mild | 2 = Severe`
- Yields a **57-dimensional feature vector** fed to the ensemble

### 🤖 Ensemble ML Model (`model.py`)
- **VotingClassifier** combining RandomForest + GradientBoosting (soft voting, weights 3:2)
- RandomForest: 200 trees, depth 20, balanced class weights, parallel jobs
- GradientBoosting: 150 estimators, depth 6, learning rate 0.08, 85% subsampling
- **114 disease classes** — from Malaria to Alzheimer's to Appendicitis
- Trained on `dataset.csv`; model cached to disk via `joblib` to avoid retraining on every app launch
- `predict_topn()` returns top-N `(disease, probability%)` tuples

### 📋 Differential Diagnosis Output
- Top 5 differentials ranked by model confidence with progress bar
- Per-differential: condition name, ICD-10 code, triage level (color-coded), specialty
- Low-confidence warning if primary prediction < 55%

### 🚦 Triage System (`disease_info.py`)
| Level | Label | Color |
|-------|-------|-------|
| CRITICAL | 🔴 Emergency — seek immediate care | Red |
| URGENT | 🟠 See a doctor within 24 hours | Orange |
| SEMI-URGENT | 🟡 GP appointment within 48–72 hours | Amber |
| ROUTINE | 🟢 Standard outpatient referral | Green |

### 🗄️ SQLite Persistence (`database.py`)
- Every prediction is inserted into a local `clinical_predictions.db`
- Stores: `session_id`, `timestamp`, symptom JSON, top-3 diagnoses, confidence, triage, specialty, ICD-10
- Analytics queries: top conditions by frequency, most reported symptoms, triage distribution
- Prediction history is exportable as a timestamped CSV

### 📊 Analytics Dashboard (Page 2)
- Total assessments, critical flags, urgent cases, unique conditions — live metrics
- Top predicted conditions leaderboard
- Most reported symptom frequency table
- Triage level bar chart across all sessions

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| UI | Streamlit (multi-page) | 3-page interactive frontend |
| ML | Scikit-learn VotingClassifier | Ensemble disease prediction |
| Data | Pandas, NumPy | Feature engineering & vector prep |
| Model Persistence | Joblib | Cache trained model to disk |
| Database | SQLite3 | Prediction history & analytics |
| Knowledge Base | Custom Python module | ICD-10, triage, red flags |
| Styling | Custom CSS (Google Fonts: DM Sans + DM Serif Display) | Clinical UI aesthetic |

---

## Project Structure

```
Disease-Prediction-Model/
│
├── app.py               # Streamlit app — 3 pages, custom CSS, full UI logic
├── model.py             # ML engine — ensemble training + predict_topn()
├── database.py          # SQLite layer — create_tables, insert, query, stats
├── disease_info.py      # Clinical knowledge — ICD-10, triage, red flags, specialties
├── dataset.csv          # Training data — 57 symptoms × 114 diseases
├── model_cache.pkl      # Serialized trained model (auto-generated)
├── clinical_predictions.db  # SQLite database (auto-generated)
└── requirements.txt     # Python dependencies
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/aryana-02/Disease-Prediction-Model.git
cd Disease-Prediction-Model

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

The app will open at `http://localhost:8501`. The model trains once on first launch and caches to `model_cache.pkl` — subsequent loads are instant.

### Dependencies

```
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## How It Works — Step by Step

```
User selects symptoms (severity 0/1/2 across 11 categories)
        │
        ▼
app.py builds a 57-dim feature vector
        │
        ▼
model.py: VotingClassifier.predict_proba() → probability per class
        │
        ▼
predict_topn() → top 5 (disease, confidence%) ranked by probability
        │
        ├──► disease_info.py: look up ICD-10, triage, red flags, specialty
        │
        ├──► database.py: INSERT prediction record into SQLite
        │
        └──► Streamlit renders differential diagnosis, triage banner,
             clinical profile, red flags, complications
```

---

## Skills Demonstrated

This project demonstrates full-stack Python engineering — not just a Jupyter notebook:

| Skill | Where |
|-------|-------|
| **Ensemble ML** | `model.py` — VotingClassifier with tuned RF + GB |
| **Feature Engineering** | 57-symptom severity matrix, categorical encoding |
| **SQL schema design** | `database.py` — normalized table, parameterized queries |
| **REST-adjacent app architecture** | Modular separation: UI / Model / DB / Knowledge |
| **Model serialization** | `joblib` cache with force-retrain flag |
| **Data aggregation queries** | `get_stats()` — GROUP BY, COUNT, multi-table logic |
| **UI/UX engineering** | Custom CSS, Google Fonts, 3-page Streamlit layout |
| **Domain knowledge encoding** | ICD-10, triage protocols, clinical red flags |

---

## Disclaimer

> ClinIQ is built for **educational and portfolio purposes only**. It is not a licensed medical device and should never replace a qualified clinician. All predictions are probabilistic and require clinical validation.

---

## Author

**Aryana Sharma** — B.Tech CSE (Health Informatics), VIT Bhopal

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aryana-sharma-284141407)
[![GitHub](https://img.shields.io/badge/GitHub-aryana--02-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/aryana-02)

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f4c81,50:1e3a5f,100:0f172a&height=100&section=footer"/>
</div>
