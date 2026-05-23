from seleniumbase import SB

PROXY = "http://sazz16014w96:t3vz152mql23@resi.fusionproxy.net:13822"

print("🚀 Test proxy diretto con SeleniumBase...")

with SB(uc=True, headless=True, xvfb=True) as sb:
    # Attiva CDP mode con proxy
    sb.activate_cdp_mode("https://api.ipify.org", proxy=PROXY)
    
    # Leggi l'IP
    ip = sb.get_text("body")
    print(f"✅ IP del browser: {ip}")
    
    # Ora prova EasyHits4U
    sb.get("https://www.easyhits4u.com/logon/")
    print(f"📍 Titolo: {sb.get_title()}")
    
    print("🎉 Successo!")
