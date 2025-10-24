📈 Customer Churn Prediction (Telco)

End-to-end machine learning system for predicting customer churn using the IBM Telco Customer Churn Dataset.
This project demonstrates the full applied ML lifecycle — from data exploration and feature engineering to model training, explainability, REST API deployment, containerization, and cloud hosting on AWS ECS (Fargate).

🧩 Project Overview

Customer churn represents customers who discontinue their services — a key metric for subscription-based businesses.
This project builds a predictive model to classify churn risk and reveal the key drivers behind customer attrition, enabling data-driven retention strategies.

🧠 Key Features

Data Preprocessing: Cleans, encodes, and scales categorical and numeric variables.

EDA: Visualizes churn trends, correlations, and customer demographics.

Modeling: Trains Logistic Regression and XGBoost models for churn prediction.

Model Tuning: Uses GridSearchCV for optimal hyperparameters and cross-validation.

Model Explainability: Leverages SHAP for transparent feature attribution.

REST API Deployment: Flask API for real-time predictions via JSON input.

Containerization: Dockerized for portability and cloud deployment.

Cloud Deployment: Hosted on AWS ECS (Fargate) for live scalable inference.

📘 Notebook Walkthrough
1️⃣ Exploratory Data Analysis (EDA)

Notebook: 01_exploratory_data_analysis.ipynb
Explores dataset structure, cleans missing values (e.g., TotalCharges), and visualizes churn trends, demographics, and imbalance.

2️⃣ Data Preprocessing & Feature Engineering

Notebook: 02_data_preprocessing_and_feature_engineering.ipynb
Encodes categorical features, scales numeric ones, and performs train/test split.
Processed datasets saved to /data/processed/ for reproducibility.

3️⃣ Model Training & Evaluation

Notebook: 03_model_training_and_evaluation.ipynb
Trains and compares:

Logistic Regression (baseline)

XGBoost (gradient-boosted tree model)

Evaluates with Accuracy, Precision, Recall, F1-score, and ROC-AUC.
Visualizes performance via confusion matrices and ROC curves.

4️⃣ Hyperparameter Tuning & Model Saving

Notebook: 04_model_tuning_and_saving.ipynb
Optimizes key XGBoost parameters:
n_estimators, max_depth, learning_rate, subsample, and colsample_bytree.

Saves the final tuned model to:

/models/xgb_churn_model.pkl

5️⃣ Model Explainability

Notebook: 05_explainability.ipynb
Explains model predictions with SHAP (SHapley Additive exPlanations).

Key Visual Outputs:

images/shap_summary_plot.png — Global feature importance

images/shap_bar_plot.png — Mean absolute feature impact

images/shap_local_explanation_5.png — Local prediction explanation

<p align="center"> <img src="images/shap_summary_plot.png" width="650" alt="Global Feature Importance"> </p>
6️⃣ REST API Deployment

Script: src/app.py
Serves the trained model as a Flask REST API for real-time churn predictions.

Endpoints

Endpoint Method Description
/health GET Returns API status
/predict POST Accepts JSON input and returns churn prediction

Example Input

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

Example Response

{
"churn_prediction": 1,
"churn_probability": 0.5144
}

7️⃣ Containerization & Cloud Deployment (AWS ECS ✅)

Dockerfile: Dockerfile
The entire Flask API is containerized and hosted on Docker Hub for cloud deployment.

Docker Image

woodskevinj/churn-api:latest

Build the image

docker build -t churn-api .

Run locally with mounted volumes

docker run -p 5050:5050 \
-v "$(pwd)/models:/app/models" \
-v "$(pwd)/data/processed:/app/data/processed" \
churn-api

Test API health

curl http://127.0.0.1:5050/health

Test prediction

curl -X POST http://127.0.0.1:5050/predict \
-H "Content-Type: application/json" \
-d '{"gender":"Female","SeniorCitizen":0,"Partner":"Yes","Dependents":"No","tenure":12,"PhoneService":"Yes","MultipleLines":"No","InternetService":"Fiber optic","OnlineSecurity":"No","OnlineBackup":"No","DeviceProtection":"Yes","TechSupport":"No","StreamingTV":"Yes","StreamingMovies":"Yes","Contract":"Month-to-month","PaperlessBilling":"Yes","PaymentMethod":"Electronic check","MonthlyCharges":79.85,"TotalCharges":941.25}'

☁️ Live AWS ECS (Fargate) Deployment

The image is hosted on Docker Hub and deployed to AWS ECS (Fargate) as a scalable REST API.

Cluster: churn-api-cluster
Service: churn-api-service
Task Definition: churn-api-task:2
Container Image: woodskevinj/churn-api:latest

Sample Health Check

curl http://<public_ip>:5050/health

Response:

{"status": "ok", "message": "Churn Prediction API is running"}

Sample Cloud Prediction

curl -X POST http://<public_ip>:5050/predict \
-H "Content-Type: application/json" \
-d '{"gender":"Female","SeniorCitizen":0,"Partner":"Yes","Dependents":"No","tenure":12,"PhoneService":"Yes","MultipleLines":"No","InternetService":"Fiber optic","OnlineSecurity":"No","OnlineBackup":"No","DeviceProtection":"Yes","TechSupport":"No","StreamingTV":"Yes","StreamingMovies":"Yes","Contract":"Month-to-month","PaperlessBilling":"Yes","PaymentMethod":"Electronic check","MonthlyCharges":79.85,"TotalCharges":941.25}'

✅ Example Output:

{
"churn_prediction": 1,
"churn_probability": 0.5144
}

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
│ ├── explainability.py # SHAP explainability ✅
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
→ Dockerfile → Docker Hub → AWS ECS (Fargate)

✅ End-to-end ML pipeline:
raw → preprocessing → training → tuning → explainability → API → container → cloud

✅ Current Progress

Data ingestion & EDA

Preprocessing pipeline

Model training & evaluation

Hyperparameter tuning & model saving

Model explainability (SHAP)

Flask REST API deployment

Dockerized container

Image pushed to Docker Hub

Deployed to AWS ECS (Fargate) 🌍

🧱 Next Steps

Add an Elastic IP or Load Balancer for a static endpoint

Implement GitHub Actions (CI/CD) for auto-deploy

Integrate CloudWatch Logs for monitoring

(Optional) Build a Streamlit dashboard for interactive predictions

📚 References

Telco Customer Churn Dataset — Kaggle

IBM Sample Data Science Dataset
