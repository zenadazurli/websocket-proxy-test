FROM python:3.11-slim

# Installa Chromium, mitmproxy e le dipendenze necessarie
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    unzip \
    curl \
    xvfb \
    && pip install mitmproxy seleniumbase \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY test_websocket.py .

# Imposta la variabile d'ambiente per indicare a SeleniumBase di usare Chromium
ENV CHROME_BIN=/usr/bin/chromium

# Avvia mitmproxy in background, aspetta, poi esegui lo script
CMD mitmdump -q --mode upstream:http://sazz16014w96:t3vz152mql23@resi.fusionproxy.net:13822 --listen-port 8080 & \
    sleep 5 && \
    python test_websocket.py
