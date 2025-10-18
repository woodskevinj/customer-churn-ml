📈 Customer Churn Prediction (Telco)

End-to-end machine learning system for predicting customer churn using the Telco Customer Churn Dataset (IBM)
.
This project demonstrates the full applied ML lifecycle — from exploratory data analysis and feature engineering to model training, explainability, containerization, and deployment.

🧩 Project Overview

Customer churn represents customers who discontinue their services — a key metric for subscription-based businesses today.
This project builds a predictive model to classify churn risk and reveal the key drivers behind customer attrition.

🧠 Key Features

Data Preprocessing: Cleans and encodes categorical/numeric variables.

EDA: Visualizes churn trends, correlations, and demographics.

Modeling: Baseline Logistic Regression and tree-based models (Random Forest, XGBoost).

Model Explainability: SHAP values for transparent feature importance and interpretability.

Containerization: Dockerized ML app for reproducibility and deployment.

Deployment-Ready: Structured to scale into an API or MLOps workflow.

🗂️ Project Structure
customer-churn-ml/
├── data/
│ └── WA*Fn-UseC*-Telco-Customer-Churn.csv
├── notebooks/
│ ├── 01_exploratory_data_analysis.ipynb
│ └── (upcoming) 02_data_preprocessing_and_feature_engineering.ipynb
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

Inside your notebook, confirm you’re running in your virtual environment:

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

Model training setup ✅

Enhanced SHAP labeling for interpretability ✅

🧱 Next Steps

Build preprocessing scripts for categorical encoding and numeric scaling

Train baseline models and evaluate performance

Integrate explainability and export SHAP plots

Containerize and deploy the model as a REST API

📚 References

Telco Customer Churn Dataset — Kaggle

IBM Sample Data Science Dataset
