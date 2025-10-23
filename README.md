📈 Customer Churn Prediction (Telco)

End-to-end machine learning system for predicting customer churn using the IBM Telco Customer Churn Dataset.
This project demonstrates the full applied ML lifecycle — from exploratory data analysis and feature engineering to model training, explainability, REST API deployment, and containerization with Docker.

🧩 Project Overview

Customer churn represents customers who discontinue their services — a key metric for subscription-based businesses today.
This project builds a predictive model to classify churn risk and reveal the key drivers behind customer attrition, enabling data-driven retention strategies.

🧠 Key Features

Data Preprocessing: Cleans and encodes categorical/numeric variables for modeling.

EDA: Visualizes churn trends, correlations, and customer demographics.

Modeling: Baseline Logistic Regression and XGBoost for churn classification.

Model Tuning: GridSearchCV for optimized hyperparameters and cross-validation.

Model Explainability: SHAP-based feature importance and interpretability for transparent model insights.

REST API Deployment: Flask API serving real-time churn predictions from JSON input.

Containerization: Dockerized application with mounted data/model volumes for reproducible deployment and portability.

📘 Notebook Walkthrough
1️⃣ Exploratory Data Analysis (EDA)

Notebook: 01_exploratory_data_analysis.ipynb
Explores dataset structure, cleans missing values (e.g., TotalCharges), and visualizes churn trends, demographics, and imbalance.

2️⃣ Data Preprocessing & Feature Engineering

Notebook: 02_data_preprocessing_and_feature_engineering.ipynb
Encodes categorical features, scales numeric ones, and performs train/test split.
Saves processed datasets into /data/processed/ for reproducibility.

3️⃣ Model Training & Evaluation

Notebook: 03_model_training_and_evaluation.ipynb
Trains Logistic Regression (baseline) and XGBoost models.
Evaluates with Accuracy, Precision, Recall, F1-score, ROC-AUC, and confusion matrices.

4️⃣ Hyperparameter Tuning & Model Saving

Notebook: 04_model_tuning_and_saving.ipynb
Optimizes XGBoost hyperparameters using GridSearchCV:

n_estimators, max_depth, learning_rate, subsample, colsample_bytree
Saves tuned model artifact to:

/models/xgb_churn_model.pkl

5️⃣ Model Explainability

Notebook: 05_explainability.ipynb
Uses SHAP (SHapley Additive exPlanations) for global and local interpretability.

Key Visual Outputs:

images/shap_summary_plot.png — Global feature impact summary

images/shap_bar_plot.png — Mean absolute SHAP values

images/shap_local_explanation_5.png — Local prediction breakdown

6️⃣ REST API Deployment

Script: src/app.py
Serves the trained model as a Flask REST API for real-time predictions.

Endpoints
Endpoint Method Description
/health GET Returns API health status
/predict POST Accepts customer JSON input and returns churn prediction

Example Input:

{
"gender": "Female",
"SeniorCitizen": 0,
"Partner": "Yes",
"Dependents": "No",
"tenure": 12,
"PhoneService": "Yes",
"MultipleLines": "No",
"InternetService": "Fiber optic",
"OnlineSecurity": "No",
"OnlineBackup": "No",
"DeviceProtection": "Yes",
"TechSupport": "No",
"StreamingTV": "Yes",
"StreamingMovies": "Yes",
"Contract": "Month-to-month",
"PaperlessBilling": "Yes",
"PaymentMethod": "Electronic check",
"MonthlyCharges": 79.85,
"TotalCharges": 941.25
}

Example Response:

{
"churn_prediction": 1,
"churn_probability": 0.5144
}

7️⃣ Containerization (New!)

Dockerfile: Dockerfile

Build and run the containerized API:

docker build -t churn-api .
docker run -p 5050:5050 \
-v "$(pwd)/models:/app/models" \
-v "$(pwd)/data/processed:/app/data/processed" \
churn-api

Verify endpoints:

curl http://127.0.0.1:5050/health

curl -X POST http://127.0.0.1:5050/predict -H "Content-Type: application/json" -d '{"gender":"Female","SeniorCitizen":0,"Partner":"Yes","Dependents":"No","tenure":12,"PhoneService":"Yes","MultipleLines":"No","InternetService":"Fiber optic","OnlineSecurity":"No","OnlineBackup":"No","DeviceProtection":"Yes","TechSupport":"No","StreamingTV":"Yes","StreamingMovies":"Yes","Contract":"Month-to-month","PaperlessBilling":"Yes","PaymentMethod":"Electronic check","MonthlyCharges":79.85,"TotalCharges":941.25}'

🗂️ Project Structure
customer-churn-ml/
├── data/
│ ├── raw/ # Original Kaggle dataset
│ └── processed/ # Encoded and scaled model-ready datasets
├── notebooks/
│ ├── 01_exploratory_data_analysis.ipynb
│ ├── 02_data_preprocessing_and_feature_engineering.ipynb
│ ├── 03_model_training_and_evaluation.ipynb
│ ├── 04_model_tuning_and_saving.ipynb
│ └── 05_explainability.ipynb
├── models/
│ └── xgb_churn_model.pkl
├── src/
│ ├── preprocessing/
│ ├── training/
│ ├── evaluation/
│ ├── explainability.py # SHAP explainability module ✅
│ └── app.py # Flask REST API ✅
├── images/
│ ├── shap_summary_plot.png
│ ├── shap_bar_plot.png
│ └── shap_local_explanation_5.png
├── requirements.txt
├── Dockerfile
└── README.md

⚙️ Getting Started
git clone https://github.com/woodskevinj/customer-churn-ml.git
cd customer-churn-ml
python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows
pip install -r requirements.txt

Launch notebooks:

jupyter notebook

🐳 Running the Dockerized API
docker build -t churn-api .
docker run -p 5050:5050 \
-v "$(pwd)/models:/app/models" \
-v "$(pwd)/data/processed:/app/data/processed" \
churn-api

Server runs at:

http://127.0.0.1:5050

📊 Model Explainability Results

Model interpretability is powered by SHAP, highlighting how each feature contributes to predictions.

<p align="center"> <img src="images/shap_summary_plot.png" width="650" alt="Global Feature Importance"> </p> <p align="center"> <img src="images/shap_local_explanation_5.png" width="650" alt="Local Prediction Explanation"> </p>
✅ Current Progress

✅ Data ingestion and EDA
✅ Preprocessing pipeline
✅ Model training & evaluation
✅ Hyperparameter tuning & model saving
✅ Model explainability with SHAP
✅ Flask REST API deployment
✅ Dockerized container with mounted data & model volumes

☁️ Next: Push container to Docker Hub or deploy to AWS ECS

🧱 Next Steps

Push container image to Docker Hub

Deploy on AWS ECS or EC2

Add CI/CD for model retraining and updates

(Optional) Build a Streamlit dashboard for real-time churn insights

🧭 Data & Model Lineage
data/raw/ → notebooks/01_eda → notebooks/02_preprocessing → data/processed/
→ notebooks/03_training → notebooks/04_tuning → models/xgb_churn_model.pkl
→ notebooks/05_explainability → src/app.py (Flask API)
→ Dockerfile → containerized API

✅ End-to-end ML workflow:
raw → preprocessing → training → tuning → explainability → deployment → containerization

📚 References

Telco Customer Churn Dataset — Kaggle

IBM Sample Data Science Dataset
