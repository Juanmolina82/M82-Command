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
        dosier = "📊 *[M82 PRIVATE MARKETS — PORTFOLIO & SECTOR ALLOCATION]* 📊\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "🏗️ *DESGLOSE POR SECTOR (TOTAL: $4,248.56M USD)*\n"
        dosier += "• *Basic Materials:* `$1,508.47M USD` (35.51% | 8 cos)\n"
        dosier += "• *Healthcare:* `$1,248.73M USD` (29.39% | 50 cos)\n"
        dosier += "• *Technology:* `$933.92M USD` (21.98% | 107 cos)\n"
        dosier += "• *Financials:* `$476.06M USD` (11.21% | 21 cos)\n"
        dosier += "• *Industrials:* `$55.99M USD` (1.32% | 21 cos)\n\n"

        dosier += "🤝 *TOP CO-INVERSORES SINDICALES*\n"
        dosier += "• *FTQ (Fonds de solidarité):* 110 Deals\n"
        dosier += "• *BDC (Business Dev Bank):* 75 Deals\n"
        dosier += "• *CDP Capital Private Equity:* 62 Deals\n"
        dosier += "• *Desjardins Capital:* 57 Deals\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Perfil sectorial y co-inversores enviados a Telegram.")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
