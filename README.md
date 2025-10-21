📈 Customer Churn Prediction (Telco)

End-to-end machine learning system for predicting customer churn using the Telco Customer Churn Dataset (IBM)
.
This project demonstrates the full applied ML lifecycle — from exploratory data analysis and feature engineering to model training, hyperparameter tuning, explainability, and deployment preparation.

🧩 Project Overview

Customer churn represents customers who discontinue their services — a key metric for subscription-based businesses today.
This project builds a predictive model to classify churn risk and reveal the key drivers behind customer attrition.

🧠 Key Features

Data Preprocessing: Cleans and encodes categorical/numeric variables.

EDA: Visualizes churn trends, correlations, and customer demographics.

Modeling: Baseline Logistic Regression and tree-based models (Random Forest, XGBoost).

Model Tuning: Uses GridSearchCV for optimized hyperparameters and cross-validation.

Model Explainability: (up next) SHAP values for transparent feature importance and interpretability.

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
Saves processed data into data/processed/ for model training and reproducibility.

3️⃣ Model Training & Evaluation

Notebook: 03_model_training_and_evaluation.ipynb
Trains and evaluates two models:

Logistic Regression (baseline)

XGBoost (gradient-boosted tree model)

Compares performance across Accuracy, Precision, Recall, F1-score, and ROC-AUC,
and visualizes model performance using confusion matrices and ROC curves.

4️⃣ Hyperparameter Tuning & Model Saving

Notebook: 04_model_tuning_and_saving.ipynb
Performs GridSearchCV with cross-validation to optimize key XGBoost hyperparameters:
n_estimators, max_depth, learning_rate, subsample, and colsample_bytree.

Saves the final tuned model to:

/models/xgb_churn_model.pkl

This step ensures reproducibility and provides a ready-to-deploy model artifact for inference.

🗂️ Project Structure
customer-churn-ml/
├── data/
│ ├── raw/ # Original Kaggle dataset
│ └── processed/ # Encoded and scaled model-ready datasets
├── notebooks/
│ ├── 01_exploratory_data_analysis.ipynb
│ ├── 02_data_preprocessing_and_feature_engineering.ipynb
│ ├── 03_model_training_and_evaluation.ipynb
│ └── 04_model_tuning_and_saving.ipynb
├── models/
│ └── xgb_churn_model.pkl
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

⚙️ Environment Verification (Optional)

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

Preprocessing pipeline ✅

Model training & evaluation ✅

Hyperparameter tuning & model saving ✅

Enhanced SHAP labeling for interpretability (next) 🚧

🧱 Next Steps

Integrate SHAP explainability notebook for feature-level insights

Generate and export SHAP summary plots to /images/

Containerize model and deploy as a REST API

(Optional) Create a lightweight Streamlit dashboard for churn predictions

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
│ X*train_processed.csv │
│ X_test_processed.csv │
│ y_train.csv / y_test.csv │
│ (Model-ready datasets) │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ notebooks/03_model_training*...│
│ - Train baseline models │
│ - Evaluate metrics │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ notebooks/04*model_tuning*... │
│ - Tune hyperparameters │
│ - Save final model (.pkl) │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ Docker / API Layer (up next) │
│ - Containerized model serving │
└────────────────────────────────┘

✅ This diagram visualizes the full ML workflow:
raw → exploration → preprocessing → model training → tuning → containerization

📚 References

Telco Customer Churn Dataset — Kaggle

IBM Sample Data Science Dataset
