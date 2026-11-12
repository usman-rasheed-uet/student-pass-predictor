# =============================================================
# Student Pass Predictor — Streamlit app
# Student: USMAN RASHEED  ·  ID: 000313
# Module 03 Project — teaching demo only
# =============================================================

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# --- Browser tab title (must be the FIRST st.* call) --------
st.set_page_config(
    page_title="Student Pass Predictor — USMAN RASHEED",
    page_icon="🎓",
    layout="centered",
)

# --- Page header: name + ID visible on the page -------------
st.title("Student Pass Predictor")
st.markdown("**USMAN RASHEED** · ID: `000313`")
st.caption("Teaching demo on synthetic data — not for real student decisions.")

# --- Load the saved pipeline (cached — loads only once) -----
@st.cache_resource
def load_pipeline():
    return joblib.load("student_pass_pipeline.joblib")

model = load_pipeline()

# --- Prediction form ---------------------------------------
with st.form("student_form"):
    hours  = st.slider("Hours studied", 0.0, 12.0, 6.0, 0.5)
    attend = st.slider("Attendance (%)", 40, 100, 80)
    tests  = st.slider("Practice tests completed", 0, 8, 3)
    sleep  = st.slider("Sleep hours", 3.0, 10.0, 7.0, 0.5)
    method = st.selectbox("Study method", ["video", "group", "self"])
    submitted = st.form_submit_button("Predict")

# --- Prediction + feature-importance chart ------------------
if submitted:
    row = pd.DataFrame([{
        "hours_studied":  hours,
        "attendance":     attend,
        "practice_tests": tests,
        "sleep_hours":    sleep,
        "study_method":   method,
    }])

    pred  = model.predict(row)[0]
    proba = model.predict_proba(row)[0, 1] if hasattr(model, "predict_proba") else None

    if pred == 1:
        st.success(f"Predicted class: Pass  (P(pass) ≈ {proba:.2f})")
    else:
        st.error(f"Predicted class: Fail  (P(pass) ≈ {proba:.2f})")

    # Feature-importance bar chart
    inner = model.named_steps["model"]

    if hasattr(inner, "feature_importances_"):
        feature_names = model.named_steps["preprocess"].get_feature_names_out()
        importances   = inner.feature_importances_
    elif hasattr(inner, "coef_"):
        feature_names = model.named_steps["preprocess"].get_feature_names_out()
        importances   = abs(inner.coef_[0])
    else:
        feature_names = None

    if feature_names is not None:
        st.subheader("What mattered most?")
        fig, ax = plt.subplots(figsize=(7, 3))
        ax.barh(feature_names, importances, color="#10b981")
        ax.set_xlabel("Importance")
        st.pyplot(fig)
        st.caption("Importance is descriptive, not a proof of cause.")

    st.info("This prediction is a classroom demo and must not be used "
            "to judge real students.")

# --- Footer signature --------------------------------------
st.divider()
st.caption("Module 03 Project · USMAN RASHEED · 000313")