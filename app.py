import streamlit as st
import pandas as pd
import pickle
from datetime import datetime

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Breast Cancer Detection",
    page_icon="🩺",
    layout="wide"
)

# ------------------------------
# Selected Features (ONLY 8)
# ------------------------------
FEATURES = [
    "radius_mean",
    "texture_mean",
    "area_mean",
    "concavity_mean",
    "concave points_mean",
    "radius_worst",
    "area_worst",
    "concave points_worst"
]

# ------------------------------
# Load Model
# ------------------------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ------------------------------
# Header
# ------------------------------
st.markdown(
    "<h1 style='text-align:center; color:#e63946;'>🧬 Breast Cancer Detection System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Decision Tree Based Clinical Prediction Tool</p>",
    unsafe_allow_html=True
)

st.divider()

# ------------------------------
# Sidebar Inputs
# ------------------------------
st.sidebar.header("🧪 Tumor Measurement Inputs")

user_input = {}
for feature in FEATURES:
    user_input[feature] = st.sidebar.number_input(
        feature.replace("_", " ").title(),
        min_value=0.0,
        value=0.0,
        format="%.4f"
    )

input_df = pd.DataFrame([user_input])

# ------------------------------
# Prediction
# ------------------------------
st.subheader("🔍 Prediction Result")

if st.button("🚀 Predict Cancer"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    report_date = datetime.now().strftime("%d %b %Y, %I:%M %p")

    diagnosis = "Malignant (Cancer Detected)" if prediction == 1 else "Benign (No Cancer)"

    # Display result
    if prediction == 1:
        st.error(f"⚠️ **{diagnosis}**")
    else:
        st.success(f"✅ **{diagnosis}**")

    # Report
    st.markdown(f"""
    ### 🧾 Diagnostic Report
    - **Diagnosis:** {diagnosis}
    - **Malignant Probability:** `{probability[1]*100:.2f}%`
    - **Benign Probability:** `{probability[0]*100:.2f}%`
    - **Model Used:** Decision Tree Classifier
    - **Report Generated:** {report_date}
    """)

    # ------------------------------
    # Download Report
    # ------------------------------
    report_df = input_df.copy()
    report_df["Diagnosis"] = diagnosis
    report_df["Malignant Probability (%)"] = probability[1] * 100
    report_df["Benign Probability (%)"] = probability[0] * 100
    report_df["Report Generated"] = report_date

    csv = report_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction Report",
        data=csv,
        file_name="cancer_prediction_report.csv",
        mime="text/csv"
    )

# ------------------------------
# Feature Importance
# ------------------------------
st.divider()
st.subheader("📊 Feature Importance")

importance_df = pd.DataFrame({
    "Feature": FEATURES,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

st.dataframe(importance_df, use_container_width=True)

# ------------------------------
# Footer
# ------------------------------
st.caption("⚕️ For educational purposes only. Not a medical diagnosis.")
