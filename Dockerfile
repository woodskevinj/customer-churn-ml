# ==========================================================
# 🐳 Customer Churn Prediction API - Dockerfile
# ==========================================================

# 1️⃣ Base Image (lightweight Python)
FROM python:3.10-slim

# 2️⃣ Set working directory inside the container
WORKDIR /app

# 3️⃣ Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ Copy the rest of the project files into the container
COPY . .

# 5️⃣ Expose Flask port
EXPOSE 5050

# 6️⃣ Set environment variables (for Flask)
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=src/app.py

# 7️⃣ Run the API
CMD ["python", "src/app.py"]
