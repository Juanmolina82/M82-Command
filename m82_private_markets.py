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
        dosier = "🏛️ *[M82 PRIVATE MARKETS — COLLER EQT DOSSIER]* 🏛️\n"
        dosier += f"💼 *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "🤝 *EVENTO M&A Y AUM GLOBAL*\n"
        dosier += "• *Estatus:* Combinación cerrada con EQT AB el 31-Ago-2026 ($3.2B + $500M earn-out).\n"
        dosier += "• *Nueva Entidad:* Coller EQT (División de Secondaries de EQT).\n"
        dosier += "• *AUM Combinado:* €341B ($389B USD) | Meta: Duplicar FAUM en 4 años.\n\n"

        dosier += "🌍 *DISTRIBUCIÓN GEOGRÁFICA ($4,248.55M USD Tracked)*\n"
        dosier += "• *Corea del Sur:* $1,500.00M (35.3%)\n"
        dosier += "• *Canadá:* $1,065.34M (25.1% | 181 cos)\n"
        dosier += "• *Finlandia:* $680.25M (16.0%)\n"
        dosier += "• *Reino Unido:* $353.77M (8.3%)\n"
        dosier += "• *EE. UU.:* $323.19M (7.6%)\n"
        dosier += "• *Países Bajos & Otros:* $326.00M (7.7%)\n\n"

        dosier += "🚪 *TRACK RECORD DE SALIDAS (EXITS)*\n"
        dosier += "• *Healthcare:* 12 Exits (PTC Therapeutics, Amphastar, Uniqure BV)\n"
        dosier += "• *Technology:* 11 Exits (Kaptivo, Touchtunes, Power Integrations)\n"
        dosier += "• *Industrials/Consumer:* 4 Exits\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Dossier consolidado enviado a Telegram con éxito.")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
