FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    firefox-esr \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY test_firefox.py .


CMD ["python", "test_firefox.py"]
