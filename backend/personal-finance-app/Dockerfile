# Simple Dockerfile for FastAPI app
FROM python:3.11-slim
WORKDIR /app

# Install dependencies
COPY requirements /app/requirements
RUN pip install --upgrade pip && pip install -r /app/requirements/base.txt

# Copy application
COPY . /app

ENV PYTHONPATH=/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
