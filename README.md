# 📈 Customer Churn Prediction (Telco)

End-to-end machine learning system for predicting customer churn using the **Telco Customer Churn dataset (IBM)**.  
This project demonstrates the full applied ML lifecycle — from exploratory data analysis and feature engineering to model training, explainability, containerization, and deployment.

---

## 🧩 Project Overview

Customer churn is a key business metric representing customers likely to discontinue their services.  
This project builds a predictive model to classify churn risk and explain key factors driving churn.

---

## 🧠 Key Features

- **Data Preprocessing:** Cleans and encodes categorical/numeric variables.
- **EDA:** Visualizes churn trends, correlations, and demographics.
- **Modeling:** Baseline Logistic Regression and tree-based models (Random Forest, XGBoost).
- **Model Explainability:** Integrated SHAP values for feature importance and interpretability.
- **Containerization:** Dockerized ML app for reproducibility and deployment.
- **Deployment-Ready:** Structured to scale into an API or MLOps workflow.

---

## 🗂️ Project Structure

customer-churn-ml/
├── data/
│ └── WA*Fn-UseC*-Telco-Customer-Churn.csv
├── notebooks/
│ └── 01_eda.ipynb
├── src/
│ ├── preprocessing/
│ ├── training/
│ └── evaluation/
├── requirements.txt
├── Dockerfile
└── README.md

yaml
Copy code

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/customer-churn-ml.git
cd customer-churn-ml
2. Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run EDA Notebook
Launch Jupyter or VS Code and open notebooks/01_eda.ipynb.

📊 Model Explainability Preview
Model interpretability is powered by SHAP visualizations to reveal how each feature contributes to churn risk.

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

Containerize and deploy model as a REST API

📚 References
Telco Customer Churn Dataset (Kaggle)

IBM Sample Data Science Dataset
```
