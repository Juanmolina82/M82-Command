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
        dosier = "📑 *[M82 PRIVATE MARKETS — PE/VC TRANSACTIONS]* 📑\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "📌 *TRANSACCIONES RECIENTES EN REFINITIV WORKSPACE*\n"
        dosier += "• *Saviynt Inc:* Tech | Acquisition | `Active` (US-CA)\n"
        dosier += "• *WorldRemit Ltd:* Tech | Later Stage | `Active` (US)\n"
        dosier += "• *Oy Medix Biochemica AB:* Healthcare | Later Stage | `Active` (FI)\n"
        dosier += "• *Ssangyong Motor Co:* Basic Materials | PIPE | `Went Public` (KR)\n"
        dosier += "• *Exterro Inc:* Tech | Recap/Turnaround | `Active` (US-OR)\n"
        dosier += "• *Vizrt Group AS:* Tech | Secondary Direct | `Active` (NO)\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Listado de transacciones enviado a Telegram.")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
