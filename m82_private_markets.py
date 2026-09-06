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
        dosier = "💼 *[M82 PRIVATE MARKETS — COLLER FOF & LP INTERESTS]* 💼\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "🤝 *POSICIONES SECUNDARIAS EN FONDOS DE TERCEROS (17 VEHÍCULOS)*\n"
        dosier += "• *Estrategia:* Adquisición de participaciones LP (Fund-of-Funds) por Coller Capital.\n"
        dosier += "• *Apollo Investment Fund X LP:* EE. UU. (Mega-Fund PE/Credit)\n"
        dosier += "• *Forbion Capital Fund I:* Países Bajos (Biotech/Healthcare)\n"
        dosier += "• *DFJ Esprit II:* Reino Unido (Tech Venture)\n"
        dosier += "• *India Advantage Fund I:* India (Mercados Emergentes)\n\n"

        dosier += "🌍 *DISTRIBUCIÓN GEOGRÁFICA DE VEHÍCULOS ADQUIRIDOS*\n"
        dosier += "• *Canadá:* 8 Fondos (47.06% — T2C2, Skypoint, GTI V, Genechem)\n"
        dosier += "• *Estados Unidos:* 5 Fondos (29.41% — Woodside, Entrepia, Apollo, Vimac)\n"
        dosier += "• *Europa (NL, UK, FR):* 3 Fondos (17.65%)\n"
        dosier += "• *Asia (IN):* 1 Fondo (5.88%)\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Registro de participaciones LP de Coller enviado a Telegram.")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
