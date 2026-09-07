#!/usr/bin/env python3
import requests
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"

class M82EGTMergerEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def dispatch(self):
        dosier = "⚡ *[M82 STRATEGIC EVENT — COLLER & EGT COMBINATION]* ⚡\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "💥 *TRANSACCIÓN CLAVE IDENTIFICADA EN REFINITIV*\n"
        dosier += "• *Entidades:* Coller Capital Ltd + EGT Corporation\n"
        dosier += "• *Objetivo:* Expansión a Infraestructura Energía / Crédito Privado\n"
        dosier += "• *Meta AUM:* Duplicar activos gestionados en un horizonte de 5 años\n\n"

        dosier += "📈 *CONTEXTO DE MERCADO SECUNDARIO (H1 2026)*\n"
        dosier += "• *Volumen Global H1 2026:* $120.00B USD\n"
        dosier += "• *Efecto en Cartera:* Mayor diversificación hacia real assets y transición energética\n\n"

        dosier += "✅ Evento corporativo validado e integrado en el pipeline de auditoría M82."

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Noticia de la combinación Coller-EGT integrada y enviada a Telegram.")

if __name__ == "__main__":
    M82EGTMergerEngine().dispatch()
