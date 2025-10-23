📈 Customer Churn Prediction (Telco)

End-to-end machine learning system for predicting customer churn using the IBM Telco Customer Churn Dataset.
This project demonstrates the full applied ML lifecycle — from data exploration and feature engineering to model training, explainability, REST API deployment, and Docker-based cloud deployment.

🧩 Project Overview

Customer churn represents customers who discontinue their services — a key metric for subscription-based businesses today.
This project builds a predictive model to classify churn risk and reveal key drivers of customer attrition, enabling data-driven retention strategies.

🧠 Key Features

Data Preprocessing: Cleans and encodes categorical/numeric variables.

EDA: Visualizes churn trends, correlations, and customer demographics.

Modeling: Baseline Logistic Regression and tuned XGBoost for churn classification.

Model Tuning: Optimizes hyperparameters with GridSearchCV and cross-validation.

Model Explainability: SHAP-based feature importance and interpretability.

REST API Deployment: Flask API serving real-time churn predictions from JSON input.

Containerization: Dockerized for portability and local/remote execution.

Cloud Deployment: Image hosted on Docker Hub for cloud integration and ECS readiness.

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
Trains and compares Logistic Regression (baseline) and XGBoost models.
Evaluates using Accuracy, Precision, Recall, F1-score, and ROC-AUC.

4️⃣ Hyperparameter Tuning & Model Saving

Notebook: 04_model_tuning_and_saving.ipynb
Performs GridSearchCV optimization for XGBoost parameters:
n_estimators, max_depth, learning_rate, subsample, colsample_bytree
Saves final tuned model to:

/models/xgb_churn_model.pkl

5️⃣ Model Explainability

Notebook: 05_explainability.ipynb
Explains model predictions with SHAP (SHapley Additive exPlanations) to enhance transparency.

Key visual outputs:

images/shap_summary_plot.png — Global feature importance

images/shap_bar_plot.png — Mean absolute feature impact

images/shap_local_explanation_5.png — Local prediction explanation

6️⃣ REST API Deployment

Script: src/app.py
Serves the trained model via Flask REST API for real-time predictions.

Endpoints
Endpoint Method Description
/health GET Returns API status
/predict POST Accepts JSON input and returns churn prediction

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

7️⃣ Containerization & Cloud Deployment (New!)

Dockerfile: Dockerfile
The Flask API is fully containerized and hosted on Docker Hub for cloud deployment.

Docker Image:
📦 woodskevinj/churn-api:latest

Build the image:

docker build -t churn-api .

Run locally with mounted volumes:

docker run -p 5050:5050 \
-v "$(pwd)/models:/app/models" \
-v "$(pwd)/data/processed:/app/data/processed" \
churn-api

Test API health:

curl http://127.0.0.1:5050/health

Test prediction:

curl -X POST http://127.0.0.1:5050/predict \
-H "Content-Type: application/json" \
-d '{"gender":"Female","SeniorCitizen":0,"Partner":"Yes","Dependents":"No","tenure":12,"PhoneService":"Yes","MultipleLines":"No","InternetService":"Fiber optic","OnlineSecurity":"No","OnlineBackup":"No","DeviceProtection":"Yes","TechSupport":"No","StreamingTV":"Yes","StreamingMovies":"Yes","Contract":"Month-to-month","PaperlessBilling":"Yes","PaymentMethod":"Electronic check","MonthlyCharges":79.85,"TotalCharges":941.25}'

Verify /app mounts:

docker exec -it <container_id> /bin/bash
ls /app/models
ls /app/data/processed

🗂️ Project Structure
customer-churn-ml/
├── data/
│ ├── raw/ # Original Kaggle dataset
│ └── processed/ # Encoded and scaled datasets
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

🧭 Workflow Overview
data/raw/ → notebooks/01_eda → notebooks/02_preprocessing → data/processed/
→ notebooks/03_training → notebooks/04_tuning → models/xgb_churn_model.pkl
→ notebooks/05_explainability → src/app.py (Flask API)
→ Dockerfile → Docker Hub → Cloud Deployment (ECS)

✅ End-to-end ML pipeline:
raw → preprocessing → training → tuning → explainability → API → container → cloud

✅ Current Progress

✅ Data ingestion & EDA
✅ Preprocessing pipeline
✅ Model training & evaluation
✅ Hyperparameter tuning & model saving
✅ Model explainability (SHAP)
✅ Flask REST API deployment
✅ Dockerized container
✅ Image pushed to Docker Hub 🌐

☁️ Next: Deploy on AWS ECS (Fargate)

🧱 Next Steps

Deploy container image on AWS ECS or EC2

Add CI/CD pipeline for continuous delivery

(Optional) Build a Streamlit dashboard for interactive churn predictions

📚 References

Telco Customer Churn Dataset — Kaggle

IBM Sample Data Science Dataset
