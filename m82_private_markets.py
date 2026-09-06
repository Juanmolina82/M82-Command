#!/usr/bin/env python3
import requests
import pandas as pd
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"

class M82PrivateMarketsEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def dispatch(self):
        dosier = "📊 *[M82 PRIVATE MARKETS — GEOGRAPHIC ALLOCATION]* 📊\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "🌍 *DESGLOSE GEOGRÁFICO DE CAPITAL (TOTAL: $4,248.55M USD)*\n"
        dosier += "• *Corea del Sur:* `$1,500.00M USD` (35.31% | 1 deal)\n"
        dosier += "• *Canadá:* `$1,065.34M USD` (25.08% | 181 cos)\n"
        dosier += "• *Finlandia:* `$680.25M USD` (16.01% | 1 co)\n"
        dosier += "• *Reino Unido:* `$353.77M USD` (8.33% | 8 cos)\n"
        dosier += "• *Estados Unidos:* `$323.19M USD` (7.61% | 23 cos)\n"
        dosier += "• *Países Bajos:* `$260.64M USD` (6.13% | 1 co)\n"
        dosier += "• *Otros (IN, DE, FR, TW):* `$65.36M USD` (1.54%)\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Desglose geográfico enviado a Telegram.")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
