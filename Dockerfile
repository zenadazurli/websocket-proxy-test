FROM python:3.11-slim

# Installa Chrome, mitmproxy e dipendenze
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /etc/apt/trusted.gpg.d/google.gpg \
    && echo "deb [arch=amd64] http://dl.google.com/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && pip install mitmproxy seleniumbase \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY test_websocket.py .

# Avvia mitmproxy in background, aspetta, poi esegui lo script
CMD mitmdump -q --mode upstream:http://sazz16014w96:t3vz152mql23@resi.fusionproxy.net:13822 --listen-port 8080 & \
    sleep 5 && \
    python test_websocket.py