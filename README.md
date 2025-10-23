📈 Customer Churn Prediction (Telco)

End-to-end machine learning system for predicting customer churn using the Telco Customer Churn Dataset (IBM).
This project demonstrates the full applied ML lifecycle — from exploratory data analysis and feature engineering to model training, hyperparameter tuning, explainability, and REST API deployment.

🧩 Project Overview

Customer churn represents customers who discontinue their services — a key metric for subscription-based businesses today.
This project builds a predictive model to classify churn risk and reveal the key drivers behind customer attrition.

🧠 Key Features

Data Preprocessing: Cleans and encodes categorical/numeric variables.

EDA: Visualizes churn trends, correlations, and customer demographics.

Modeling: Baseline Logistic Regression and XGBoost for churn classification.

Model Tuning: Uses GridSearchCV for optimized hyperparameters and cross-validation.

Model Explainability: SHAP-based feature importance and interpretability for transparent decision-making.

REST API Deployment: Flask API serving live churn predictions from JSON input.

Containerization (up next): Prepares the API for Docker and cloud deployment.

📘 Notebook Walkthrough
1️⃣ Exploratory Data Analysis (EDA)

Notebook: 01_exploratory_data_analysis.ipynb
Explores dataset structure, cleans missing values (notably TotalCharges), and visualizes churn trends.
Includes demographic distributions, churn imbalance visualization, and early insight extraction.

2️⃣ Data Preprocessing & Feature Engineering

Notebook: 02_data_preprocessing_and_feature_engineering.ipynb
Encodes categorical features, scales numerical ones, and performs train/test split.
Saves processed data into /data/processed/ for model training and reproducibility.

3️⃣ Model Training & Evaluation

Notebook: 03_model_training_and_evaluation.ipynb
Trains and evaluates two models:

Logistic Regression (baseline)

XGBoost (gradient-boosted tree model)

Compares Accuracy, Precision, Recall, F1-score, and ROC-AUC.
Visualizes model performance with confusion matrices and ROC curves.

4️⃣ Hyperparameter Tuning & Model Saving

Notebook: 04_model_tuning_and_saving.ipynb
Performs GridSearchCV with cross-validation to optimize key XGBoost hyperparameters:
n_estimators, max_depth, learning_rate, subsample, colsample_bytree.

Saves the final tuned model to:

/models/xgb_churn_model.pkl

5️⃣ Model Explainability

Notebook: 05_explainability.ipynb
Explains model predictions using SHAP (SHapley Additive exPlanations).
Generates global and local feature importance plots that visualize how the model evaluates churn risk.

Key visual outputs:

images/shap_summary_plot.png — Global feature impact summary

images/shap_bar_plot.png — Mean absolute SHAP values

images/shap_local_explanation_5.png — Local prediction explanation

6️⃣ REST API Deployment (New!)

Script: src/app.py
Serves the trained model as a Flask REST API.

Endpoints:

Endpoint Method Description
/health GET Returns API status
/predict POST Accepts customer JSON input and returns churn prediction

Example JSON input:

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

Example response:

{
"churn_prediction": 1,
"churn_probability": 0.5144
}

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
│ └── app.py # Flask REST API for churn prediction ✅
├── images/
│ ├── shap_summary_plot.png
│ ├── shap_bar_plot.png
│ └── shap_local_explanation_5.png
├── requirements.txt
├── Dockerfile (coming soon)
└── README.md

🚀 Getting Started
1️⃣ Clone Repository
git clone https://github.com/woodskevinj/customer-churn-ml.git
cd customer-churn-ml

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Launch Jupyter Notebook
jupyter notebook

Then open:
notebooks/01_exploratory_data_analysis.ipynb

⚙️ Running the Flask API

Start the API:

python src/app.py

Server runs on:

http://127.0.0.1:5050

Test endpoints:

curl http://127.0.0.1:5050/health

✅ Returns:

{"status": "ok", "message": "Churn Prediction API is running"}

Send a test prediction:

curl -X POST http://127.0.0.1:5050/predict \
-H "Content-Type: application/json" \
-d '{"gender":"Female","SeniorCitizen":0,"Partner":"Yes","Dependents":"No","tenure":12,"PhoneService":"Yes","MultipleLines":"No","InternetService":"Fiber optic","OnlineSecurity":"No","OnlineBackup":"No","DeviceProtection":"Yes","TechSupport":"No","StreamingTV":"Yes","StreamingMovies":"Yes","Contract":"Month-to-month","PaperlessBilling":"Yes","PaymentMethod":"Electronic check","MonthlyCharges":79.85,"TotalCharges":941.25}'

📊 Model Explainability Results

Model interpretability is powered by SHAP visualizations that highlight how each feature contributes to churn predictions.

<p align="center"> <img src="images/shap_summary_plot.png" width="650" alt="Global Feature Importance"> </p> <p align="center"> <img src="images/shap_local_explanation_5.png" width="650" alt="Local Prediction Explanation"> </p>
✅ Current Progress

Data ingestion and EDA ✅

Preprocessing pipeline ✅

Model training & evaluation ✅

Hyperparameter tuning & model saving ✅

Model explainability with SHAP ✅

Flask REST API deployment ✅

Containerization (next) 🚧

🧱 Next Steps

Create a Dockerfile and containerize the Flask API

Deploy container on AWS ECS or EC2

Integrate CI/CD for retraining and monitoring

(Optional) Create a Streamlit dashboard for interactive churn insights

🧭 Project-Level Data & Model Lineage
data/raw/ → notebooks/01_eda → notebooks/02_preprocessing → data/processed/
→ notebooks/03_training → notebooks/04_tuning → models/xgb_churn_model.pkl
→ notebooks/05_explainability → src/app.py (REST API) → Docker/API layer

✅ Visualizes the full ML workflow:
raw → preprocessing → training → tuning → explainability → deployment → containerization

📚 References

Telco Customer Churn Dataset — Kaggle

IBM Sample Data Science Dataset
