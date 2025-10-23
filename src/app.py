"""
app.py
-------
Flask REST API for Customer Churn Prediction

Endpoints:
- /health: quick API health check
- /predict: accespt JSON input and returns churn prediction + probability
"""

from flask import Flask, request, jsonify
import joblib
import pandas as pd
import traceback
from pathlib import Path

# ------------------------------------------------------------
# 1️⃣ Initialize Flask app
# ------------------------------------------------------------
app = Flask(__name__)

# ------------------------------------------------------------
# 2️⃣ Load the trained model
# ------------------------------------------------------------
MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "xgb_churn_model.pkl"
model = joblib.load(MODEL_PATH)

# ------------------------------------------------------------
# 3️⃣ Health check endpoint
# ------------------------------------------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "Churn Prediction API is running"}), 200

# ------------------------------------------------------------
# 4️⃣ Prediction endpoint
# ------------------------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data
        data = request.get_json()

        # Conver input JSON to DataFrame
        X_input = pd.DataFrame([data])

        # Load training feature structure to ensure correct columns
        PROCESSED_PATH = Path(__file__).resolve().parents[1] / "data" / "processed" / "X_train_processed.csv"
        X_train_cols = pd.read_csv(PROCESSED_PATH, nrows=1).columns.tolist()

        # Convert categorical to dummy variables
        X_encoded = pd.get_dummies(X_input)

        # Align columns with training data
        X_aligned = X_encoded.reindex(columns=X_train_cols, fill_value=0)

        # Convert all dtypes to float32 (required by XGBoost)
        X_aligned = X_aligned.astype("float32")

        # Make prediction
        prediction = model.predict(X_aligned)[0]
        probability = model.predict_proba(X_aligned)[0][1] # churn probability

        # Return results
        result = {
            "churn_prediction": int(prediction),
            "churn_probability": round(float(probability), 4)
        }
        return jsonify(result), 200
    
    except Exception as e:
        print("❌ Error during prediction:", e)
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500
    
# ------------------------------------------------------------
# 5️⃣ Run the Flask app
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)