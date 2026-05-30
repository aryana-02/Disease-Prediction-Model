import sqlite3
import json
from datetime import datetime

DB_PATH = "clinical_predictions.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_conn()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS predictions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp   TEXT NOT NULL,
            symptoms    TEXT NOT NULL,          -- JSON of symptom: value
            top1        TEXT,
            top2        TEXT,
            top3        TEXT,
            confidence  REAL,
            triage      TEXT,
            specialty   TEXT,
            icd10       TEXT,
            session_id  TEXT
        );

        CREATE TABLE IF NOT EXISTS symptom_analytics (
            symptom     TEXT PRIMARY KEY,
            total_count INTEGER DEFAULT 0,
            last_seen   TEXT
        );
    """)
    conn.commit()
    conn.close()

def insert_prediction(symptom_dict, top_predictions, triage, specialty, icd10, session_id=""):
    conn = get_conn()
    ts = datetime.now().isoformat()
    tops = [p[0] for p in top_predictions] + ["", "", ""]
    confs = [p[1] for p in top_predictions] + [0, 0, 0]
    conn.execute("""
        INSERT INTO predictions
        (timestamp, symptoms, top1, top2, top3, confidence, triage, specialty, icd10, session_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (ts, json.dumps(symptom_dict), tops[0], tops[1], tops[2], confs[0], triage, specialty, icd10, session_id))

    # Update symptom analytics
    for sym, val in symptom_dict.items():
        if val > 0:
            conn.execute("""
                INSERT INTO symptom_analytics (symptom, total_count, last_seen)
                VALUES (?, 1, ?)
                ON CONFLICT(symptom) DO UPDATE SET
                    total_count = total_count + 1,
                    last_seen = excluded.last_seen
            """, (sym, ts))
    conn.commit()
    conn.close()

def get_all_predictions(limit=200):
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM predictions ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_stats():
    conn = get_conn()
    total     = conn.execute("SELECT COUNT(*) FROM predictions").fetchone()[0]
    by_dis    = conn.execute(
        "SELECT top1, COUNT(*) as cnt FROM predictions GROUP BY top1 ORDER BY cnt DESC LIMIT 10"
    ).fetchall()
    by_triage = conn.execute(
        "SELECT triage, COUNT(*) as cnt FROM predictions GROUP BY triage"
    ).fetchall()
    top_syms  = conn.execute(
        "SELECT symptom, total_count FROM symptom_analytics ORDER BY total_count DESC LIMIT 10"
    ).fetchall()
    conn.close()
    return {
        "total": total,
        "by_disease": [dict(r) for r in by_dis],
        "by_triage":  [dict(r) for r in by_triage],
        "top_symptoms": [dict(r) for r in top_syms],
    }
