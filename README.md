🧬 Breast Cancer Detection System

A machine learning–powered clinical decision support system built using a Decision Tree Classifier to predict whether a breast tumor is Benign or Malignant based on tumor measurement features.
The application is deployed using Streamlit with an interactive UI for real-time predictions and feature importance analysis.


🚀 Features

🔢 Interactive tumor measurement inputs

🌳 Decision Tree–based classification

📊 Prediction probabilities (Benign vs Malignant)

📈 Feature importance visualization

📝 Auto-generated diagnostic report

⬇️ Downloadable prediction report

🌙 Modern dark-themed Streamlit UI

🖥️ Application Interface


first (https://github.com/SanjivaniS10/Breast_Cancer_detection/blob/main/Screenshot%202025-12-27%20234247.png)

Second (https://github.com/SanjivaniS10/Breast_Cancer_detection/blob/main/Screenshot%202025-12-27%20225148.png)


🔍 Tumor Measurement Inputs

Users can input values for key tumor features such as:

Radius Mean

Texture Mean

Area Mean

Concavity Mean

Concave Points Mean

Radius Worst

Area Worst

Concave Points Worst

🧪 Prediction Output

Diagnosis: Benign / Malignant

Malignant Probability (%)

Benign Probability (%)

Model Used: Decision Tree Classifier

Timestamped Diagnostic Report

📊 Feature Importance

The model highlights which features contributed most to the prediction, improving interpretability and trust in the results.

🛠️ Tech Stack
Category	Tools
Programming Language	Python
ML Model	Decision Tree Classifier
Libraries	Pandas, NumPy, Scikit-learn
Web Framework	Streamlit
Model Serialization	Pickle
Visualization	Streamlit Components
📂 Project Structure
Breast-Cancer-Detection/
│
├── app.py                     # Streamlit application
├── model.pkl                  # Trained Decision Tree model
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── data/
    └── breast_cancer.csv      # Dataset (optional)

📊 Dataset

Source: Breast Cancer Wisconsin (Diagnostic) Dataset

Features Used: Selected mean and worst tumor measurements

Target Classes:

0 → Benign

1 → Malignant

🎯 Model Details

Algorithm: Decision Tree Classifier

Why Decision Tree?

Easy to interpret

Handles non-linearity well

Feature importance support

Evaluation Metrics:

Accuracy

Precision

Recall

Probability Scores

📈 Future Improvements

Add cross-validation and hyperparameter tuning

Support multiple ML models (Random Forest, XGBoost)

Integrate SHAP for explainability

Deploy on cloud (Streamlit Cloud / AWS)

Add user authentication

👩‍💻 Author

Sanjivani Santosh Suryawanshi
🎓 Data Science & Data Analysis Student
💡 Interested in Machine Learning, Analytics, and AI Applications
