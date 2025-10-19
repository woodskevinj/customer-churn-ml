📈 Customer Churn Prediction (Telco)

End-to-end machine learning system for predicting customer churn using the Telco Customer Churn Dataset (IBM)
.
This project demonstrates the full applied ML lifecycle — from exploratory data analysis and feature engineering to model training, explainability, containerization, and deployment.

🧩 Project Overview

Customer churn represents customers who discontinue their services — a key metric for subscription-based businesses today.
This project builds a predictive model to classify churn risk and reveal the key drivers behind customer attrition.

🧠 Key Features

Data Preprocessing: Cleans and encodes categorical/numeric variables.

EDA: Visualizes churn trends, correlations, and customer demographics.

Modeling: Baseline Logistic Regression and tree-based models (Random Forest, XGBoost).

Model Explainability: SHAP values for transparent feature importance and interpretability.

Containerization: Dockerized ML app for reproducibility and deployment.

Deployment-Ready: Structured to scale into an API or MLOps workflow.

📘 Notebook Walkthrough
1️⃣ Exploratory Data Analysis (EDA)

Notebook: 01_exploratory_data_analysis.ipynb
Explores dataset structure, cleans missing values (notably TotalCharges), and visualizes churn trends.
Includes demographic distributions, churn imbalance visualization, and early insight extraction.

2️⃣ Data Preprocessing & Feature Engineering

Notebook: 02_data_preprocessing_and_feature_engineering.ipynb
Encodes categorical features, scales numerical ones, and performs train/test split.
Saves processed data into data/processed/ for model training and future reproducibility.

3️⃣ Model Training & Evaluation

Notebook: 03_model_training_and_evaluation.ipynb
Trains and evaluates two models:

Logistic Regression (baseline)

XGBoost (gradient-boosted tree model)

Compares metrics like Accuracy, Precision, Recall, F1-score, and ROC-AUC.
Visualizes performance using confusion matrices and ROC curves for each model.

🗂️ Project Structure
customer-churn-ml/
├── data/
│ ├── raw/ # Original Kaggle dataset
│ └── processed/ # Encoded and scaled model-ready datasets
├── notebooks/
│ ├── 01_exploratory_data_analysis.ipynb
│ ├── 02_data_preprocessing_and_feature_engineering.ipynb
│ └── 03_model_training_and_evaluation.ipynb
├── src/
│ ├── preprocessing/
│ ├── training/
│ └── evaluation/
├── requirements.txt
├── Dockerfile
└── README.md

🚀 Getting Started
1️⃣ Clone Repository
git clone https://github.com/woodskevinj/customer-churn-ml.git
cd customer-churn-ml

2️⃣ Create Virtual Environment
python -m venv venv

# Activate:

source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Launch Jupyter Notebook
jupyter notebook

Then open:

notebooks/01_exploratory_data_analysis.ipynb

⚙️ Environment Verification (Optional but Recommended)

Inside your notebook, confirm you’re running inside your virtual environment:

import sys
print(sys.executable)

Expected output:

.../customer-churn-ml/venv/bin/python

📊 Model Explainability Preview

Model interpretability is powered by SHAP visualizations that highlight how each feature contributes to churn predictions.

<p align="center"> <img src="images/shap_summary.png" width="650" alt="Model Explainability Preview"> </p>
✅ Current Progress

Data ingestion and EDA ✅

Initial preprocessing pipeline ✅

Model training and evaluation ✅

Enhanced SHAP labeling for interpretability ✅

🧱 Next Steps

Perform hyperparameter tuning for XGBoost

Add model persistence (save .joblib model to /models/)

Integrate explainability notebook using SHAP visualizations

Containerize and deploy as a REST API

🧭 Project-Level Data & Model Lineage Diagram
┌────────────────────────────────┐
│ data/raw/ │
│ (Original Kaggle dataset) │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ notebooks/01*exploratory*... │
│ Exploratory Data Analysis │
│ - Inspect & clean data │
│ - Identify churn drivers │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ notebooks/02*data_preproc*... │
│ Feature Engineering │
│ - Encode categorical vars │
│ - Scale numeric vars │
│ - Train/test split │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ data/processed/ │
│ X*train.csv / X_test.csv │
│ y_train.csv / y_test.csv │
│ (Model-ready datasets) │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ notebooks/03_model*... │
│ - Train ML models │
│ - Evaluate metrics │
│ - Generate SHAP explanations │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ Docker / API Layer │
│ - Containerized app for │
│ model inference & serving │
└────────────────────────────────┘

✅ This diagram visualizes the full ML workflow:
raw → exploration → preprocessing → model training → containerized deployment

It shows end-to-end data movement and how each part of the repo contributes to the applied ML pipeline.

📚 References

Telco Customer Churn Dataset — Kaggle

IBM Sample Data Science Dataset
