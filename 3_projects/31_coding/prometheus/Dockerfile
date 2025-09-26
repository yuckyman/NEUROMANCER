FROM python:3.11-slim

# set working directory
WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# copy requirements and install python dependencies
COPY requirements_prometheus.txt .
RUN pip install --no-cache-dir -r requirements_prometheus.txt

# copy application code
COPY . .

# create directories for data and logs
RUN mkdir -p prometheus_data prometheus_logs prometheus_models

# set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# expose port for dashboard (if we add one)
EXPOSE 8080

# run prometheus
CMD ["python", "run_prometheus.py"]
