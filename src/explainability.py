"""
explainability.py
-----------------
Generates SHAP-based explainability visualizations for the Telco Customer Churn model.
This script loads the final trained XGBoost model, computes SHAP values,
and exports global and local interpretability plots to /images/.

Usage:
    python src/explainability.py
"""

import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def load_data():
    """Load processed test data."""
    X_test = pd.read_csv("data/processed/X_test_processed.csv")
    y_test = pd.read_csv("data/processed/y_test.csv").values.ravel()
    return X_test, y_test

def load_model():
    """Load the final trained model."""
    model = joblib.load("models/xgb_churn_model.pkl")
    return model

def generate_shap_plots(model, X_test):
    """Generate and save SHAP plots."""
    #Path("images").mkdir(exist_ok=True)
    ROOT_DIR = Path(__file__).resolve().parents[1]
    IMAGE_DIR = ROOT_DIR / "images"
    IMAGE_DIR.mkdir(exist_ok=True)


    # Initialize explainer
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)

    # Global feature importance
    shap.summary_plot(shap_values, X_test, show=False)
    plt.tight_layout
    plt.savefig(IMAGE_DIR / "shap_summary_plot.png", bbox_inches="tight")
    plt.close()

    shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
    plt.tight_layout
    plt.savefig(IMAGE_DIR / "shap_bar_plot.png", bbox_inches="tight")
    plt.close()

    # Local explanation
    sample_index = 5
    shap.plots.waterfall(
        shap.Explanation(
            values=shap_values[sample_index],
            base_values=explainer.expected_value,
            data=X_test.iloc[sample_index],
            feature_names=X_test.columns,
        ),
    show=False
    )
    plt.tight_layout
    plt.savefig(IMAGE_DIR / "shap_local_explanation.png", bbox_inches="tight")
    plt.close()

    print("✅ SHAP explainability plots saved to /images/")

def main():
    print("🔍 Starting model explainability process...")
    X_test, y_test = load_data()
    model = load_model()
    generate_shap_plots(model, X_test)
    print("✅ Model explainability complete.")

if __name__ == "__main__":
    main()

