
FROM python:3.12-slim

WORKDIR /app

# System deps for mysqlclient and healthcheck
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy app
COPY . /app

# Install Python deps
RUN pip install --no-cache-dir \
    flask \
    flask-sqlalchemy \
    flask-login \
    flask-migrate \
    mysqlclient

EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

CMD ["python", "app.py"]
