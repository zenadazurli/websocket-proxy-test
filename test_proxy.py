from seleniumbase import SB

PROXY = "http://sazz16014w96:t3vz152mql23@resi.fusionproxy.net:13822"

# Usa browser="chrome" esplicitamente, senza uc=True
with SB(browser="chrome", headless=True, xvfb=True, proxy=PROXY) as sb:
    sb.open("https://api.ipify.org")
    ip = sb.get_text("body")
    print(f"✅ IP del browser: {ip}")