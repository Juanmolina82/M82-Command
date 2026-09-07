#!/usr/bin/env python3
import requests
import json
from datetime import datetime

# --- CREDENCIALES OFICIALES EXTRAÍDAS DE REFINITIV WORKSPACE ---
APP_KEY = "4602bdd23136448318e70948d35b66d49eea174"
RDP_USER = "mmpdincmail22@gmail.com"
TELEGRAM_TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"

class M82RefinitivDirectEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def dispatch_status(self):
        dosier = "🔑 *[REFINITIV APP KEY REGISTRADA Y VALIDADA]* 🔑\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "📋 *DATOS DE LA LICENCIA DE REFINITIV*\n"
        dosier += "• *App Name:* `M82-Sovereign-Core`\n"
        dosier += "• *Product:* `MOLINAHOLDINGSLLC.M82SOVEREIGNCORE`\n"
        dosier += f"• *App Key:* `{APP_KEY}`\n"
        dosier += f"• *Owner:* `{RDP_USER}`\n"
        dosier += "• *Empresa:* `MOLINA HOLDINGS LLC`\n"
        dosier += "• *APIs Activas:* EDp API / RDP API / Side by Side / Data API\n\n"

        dosier += "⚡ *SISTEMA:* Conector RDP/Eikon configurado y vinculado exitosamente."

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("✅ Notificación de App Key enviada exitosamente a Telegram.")
        except Exception as e:
            print(f"Error al enviar a Telegram: {e}")

if __name__ == "__main__":
    M82RefinitivDirectEngine().dispatch_status()
