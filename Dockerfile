# Dockerfile

# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code, model, and data
COPY src/ src/
COPY models/ models/
COPY data/processed/ data/processed/

# Expose Flask port
EXPOSE 5050

# Run the app
CMD ["python", "src/app.py"]
