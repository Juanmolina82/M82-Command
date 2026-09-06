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
        dosier = "📊 *[M82 PRIVATE MARKETS — STAGE ALLOCATION]* 📊\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "🚀 *DESGLOSE POR ETAPA DE INVERSIÓN (STAGE)*\n"
        dosier += "• *PIPE:* `$1,508.14M USD` (35.50% | Avg: $251.36M/co)\n"
        dosier += "• *Later Stage:* `$1,353.92M USD` (31.87% | Avg: $56.41M/co)\n"
        dosier += "• *VC Partnership:* `$475.25M USD` (11.19% | Avg: $27.96M/co)\n"
        dosier += "• *Expansion:* `$447.56M USD` (10.54% | 99 cos)\n"
        dosier += "• *Early Stage:* `$366.97M USD` (8.64% | 96 cos)\n"
        dosier += "• *Seed & Otras:* `$96.09M USD` (2.26%)\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Desglose por etapas de inversión enviado a Telegram.")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
