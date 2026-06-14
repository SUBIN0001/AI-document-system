FROM python:3.10-slim

# Install build dependencies for libraries like easyocr/numpy if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY . .

# Create the uploads directory
RUN mkdir -p uploads

# Expose the default FastAPI port
EXPOSE 8000

# Start Celery worker in the background and FastAPI (uvicorn) in the foreground
CMD celery -A celery_worker.celery_app worker --loglevel=info & uvicorn main:app --host 0.0.0.0 --port $PORT
