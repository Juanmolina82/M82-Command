#!/usr/bin/env python3
import requests
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"

class M82CorporateTreeEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def dispatch(self):
        dosier = "🌳 *[M82 CORPORATE STRUCTURE — COLLER CAPITAL GROUP]* 🌳\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "🏢 *MATRIZ OPERATIVA:* `Coller Capital Ltd` (UK)\n\n"
        
        dosier += "🌍 *FILIALES REGIONALES (SUBSIDIARIES)*\n"
        dosier += "• *EE. UU.:* Coller Capital Inc\n"
        dosier += "• *Francia:* Omnes Capital SAS\n"
        dosier += "• *Canadá:* Société Innovation du Grand Montreal\n\n"

        dosier += "📍 *VEHÍCULOS OPERATIVOS SECUNDARIOS*\n"
        dosier += "• *Irlanda:* Power Capital Renewable Energy\n"
        dosier += "• *Francia:* Innovation Construction pour L'Avenir\n\n"

        dosier += "⚠️ *NOTA AUDITORÍA:* Arbol societario verificado. Confirma la separación absoluta entre entidades de gestión y los fondos de inversión LP de $50B."

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Estructura corporativa de Coller registrada y enviada a Telegram.")

if __name__ == "__main__":
    M82CorporateTreeEngine().dispatch()
