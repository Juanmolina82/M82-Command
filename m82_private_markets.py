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
        dosier = "🚪 *[M82 PRIVATE MARKETS — PE/VC EXITS TRACKER]* 🚪\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "💰 *DESINVERSIONES Y LIQUIDACIONES HISTÓRICAS*\n"
        dosier += "• *Healthcare / Bio:* 12 Exits (PTC Therapeutics, Amphastar, Uniqure BV)\n"
        dosier += "• *Technology:* 11 Exits (Kaptivo, Touchtunes, Power Integrations, Icera)\n"
        dosier += "• *Industrials & Services:* 4 Exits (ThermoCeramics, Foundation Partners)\n\n"
        dosier += "🌍 *Mercados de Salida Principales:* Canadá (Quebec), EE. UU. (CA, NY, MA) y Europa (UK, NL, NO).\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Registro de desinversiones (Exits) enviado a Telegram.")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
