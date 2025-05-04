FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a non-root user to run the application
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Install system dependencies and Terraform
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        unzip \
        ca-certificates \
        procps \ 
        coreutils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create and set working directory
RUN mkdir -p /frontend
WORKDIR /frontend

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ src/
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Create a directory for user-provided config
RUN mkdir -p /config \
    && chown -R appuser:appuser /config

RUN chown -R appuser:appuser /frontend

# Switch to non-root user
USER appuser

# Set default command to run with uvicorn directly
ENTRYPOINT ["./entrypoint.sh"]

# Documentation in the form of labels
LABEL maintainer="yoyobesser" \
      project="yotla-frontend" \