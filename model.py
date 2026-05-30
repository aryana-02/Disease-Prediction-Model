import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib
import os

SYMPTOMS = [
    "fever", "cough", "headache", "fatigue", "body_pain",
    "sore_throat", "runny_nose", "shortness_of_breath", "chest_pain", "nausea",
    "vomiting", "diarrhea", "constipation", "abdominal_pain", "loss_of_appetite",
    "weight_loss", "weight_gain", "joint_pain", "muscle_weakness", "skin_rash",
    "itching", "swelling", "dizziness", "confusion", "memory_loss",
    "blurred_vision", "eye_redness", "ear_pain", "hearing_loss", "tinnitus",
    "neck_stiffness", "back_pain", "frequent_urination", "painful_urination", "blood_in_urine",
    "jaundice", "pale_stools", "dark_urine", "bleeding", "nosebleed",
    "palpitations", "irregular_heartbeat", "cold_sweats", "night_sweats", "hair_loss",
    "dry_skin", "excessive_thirst", "excessive_hunger", "numbness", "tingling",
    "tremors", "seizures", "loss_of_consciousness", "anxiety", "depression",
    "insomnia", "lymph_node_swelling", "bruising", "mouth_ulcers",
]

SYMPTOM_CATEGORIES = {
    "General / Constitutional":    ["fever", "fatigue", "body_pain", "weight_loss", "weight_gain", "night_sweats", "cold_sweats"],
    "Respiratory":                 ["cough", "shortness_of_breath", "sore_throat", "runny_nose"],
    "Cardiovascular":              ["chest_pain", "palpitations", "irregular_heartbeat"],
    "Gastrointestinal":            ["nausea", "vomiting", "diarrhea", "constipation", "abdominal_pain",
                                    "loss_of_appetite", "jaundice", "pale_stools", "dark_urine", "bleeding", "mouth_ulcers"],
    "Neurological / Psychiatric":  ["headache", "dizziness", "confusion", "memory_loss", "seizures",
                                    "loss_of_consciousness", "tremors", "numbness", "tingling",
                                    "neck_stiffness", "anxiety", "depression", "insomnia"],
    "Musculoskeletal":             ["joint_pain", "muscle_weakness", "back_pain", "swelling"],
    "Dermatological":              ["skin_rash", "itching", "hair_loss", "dry_skin"],
    "Urological / Renal":          ["frequent_urination", "painful_urination", "blood_in_urine"],
    "Ophthalmic / ENT":            ["blurred_vision", "eye_redness", "ear_pain", "hearing_loss", "tinnitus"],
    "Haematological":              ["nosebleed", "bruising", "lymph_node_swelling"],
    "Endocrine / Metabolic":       ["excessive_thirst", "excessive_hunger", "hot_flashes"],
}

MODEL_CACHE = "model_cache.pkl"

def train_model(force_retrain=False):
    print("Starting training...")

    if not force_retrain and os.path.exists(MODEL_CACHE):
        print("Loading cached model")
        return joblib.load(MODEL_CACHE)

    df = pd.read_csv("dataset.csv")
    print("Dataset loaded")

    X = df[SYMPTOMS]
    print("Features extracted")

    y = df["disease"]
    print("Target extracted")

    rf  = RandomForestClassifier(n_estimators=200, max_depth=20, min_samples_leaf=2,
                                 class_weight="balanced", random_state=42, n_jobs=-1)

    gb  = GradientBoostingClassifier(n_estimators=150, max_depth=6,
                                     learning_rate=0.08, subsample=0.85,
                                     random_state=42)

    svm = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", SVC(kernel="rbf", C=5, gamma="scale",
                    probability=True,
                    class_weight="balanced",
                    random_state=42))
    ])

    ensemble = VotingClassifier(
        estimators=[("rf", rf), ("gb", gb)],
        voting="soft",
        weights=[3, 2]
    )

    print("Starting model fit...")
    ensemble.fit(X, y)
    print("Training complete")

    joblib.dump(ensemble, MODEL_CACHE)
    print("Model saved")

    return ensemble


def predict_topn(model, symptom_vector, n=5):
    """Return top-N (disease, probability) predictions."""
    proba = model.predict_proba([symptom_vector])[0]
    classes = model.classes_
    top_idx = np.argsort(proba)[::-1][:n]
    return [(classes[i], float(proba[i]) * 100) for i in top_idx]
