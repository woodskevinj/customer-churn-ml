📂 Data Directory

This folder contains all datasets used throughout the Customer Churn Prediction (Telco) project.
It follows a standard data science directory convention for reproducibility, clarity, and data lineage tracking.

🧱 Folder Structure
data/
├── raw/ # Original, unmodified data downloaded from Kaggle
├── processed/ # Cleaned, encoded, and scaled data used for model training
└── README.md # This file

🧠 Folder Details
1️⃣ raw/

Contains the original dataset:
WA*Fn-UseC*-Telco-Customer-Churn.csv

Downloaded directly from Kaggle:
Telco Customer Churn Dataset (IBM)

Serves as the source of truth for all downstream notebooks.

Do not modify this file — keep it intact to maintain data integrity.

2️⃣ processed/

Contains the transformed datasets created during preprocessing and feature engineering.

Files include:

X_train.csv, X_test.csv – Encoded and scaled feature sets

y_train.csv, y_test.csv – Corresponding churn labels

Generated automatically by the notebook:
notebooks/02_data_preprocessing_and_feature_engineering.ipynb

⚙️ Workflow Summary

Raw data → loaded from data/raw/WA*Fn-UseC*-Telco-Customer-Churn.csv

Exploratory Data Analysis (EDA) → performed in Notebook 01

Feature Engineering & Preprocessing → executed in Notebook 02

Processed data → exported to data/processed/ for modeling

🚫 Version Control Notice

Both /data/raw/ and /data/processed/ are excluded from Git tracking via .gitignore to:

Avoid uploading large or private datasets

Keep repository size manageable

Encourage reproducible local data generation

✅ Tip:
If you clone this project, download the original dataset from Kaggle and place it in data/raw/ before running the notebooks.

🧭 Data Lineage Diagram
┌────────────────────────────────┐
│ data/raw/ │
│ ─────────────────────────── │
│ WA*Fn-UseC*-Telco-...csv │
│ (Original Kaggle dataset) │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ notebooks/01*exploratory*... │
│ Exploratory Data Analysis │
│ - Inspect & clean data │
│ - Convert TotalCharges │
│ - Identify churn drivers │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ notebooks/02*data_preproc*...│
│ Feature Engineering │
│ - Encode categorical features │
│ - Scale numerical features │
│ - Train/test split │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ data/processed/ │
│ ──────────────────────────── │
│ X_train.csv / X_test.csv │
│ y_train.csv / y_test.csv │
│ (Model-ready datasets) │
└──────────────┬─────────────────┘
│
▼
┌────────────────────────────────┐
│ src/training/ & src/eval/ │
│ - Train ML models │
│ - Evaluate performance │
│ - Generate SHAP explanations │
└────────────────────────────────┘

✅ This visual shows the data lifecycle:
raw → cleaned → processed → model-ready → evaluated

It ties your notebooks, data folders, and source code into one clear, reproducible pipeline.
