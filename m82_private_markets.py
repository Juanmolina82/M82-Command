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
        dosier = "💼 *[M82 PRIVATE MARKETS — COLLER SECONDARY LP PORTFOLIO]* 💼\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "🏛️ *CARTERA DE FONDOS SECUNDARIOS (COLLER CAPITAL)*\n"
        dosier += "• *Estatus:* Participaciones LP adquiridas vía mercado secundario.\n"
        dosier += "• *Apollo Investment Fund X LP:* EE. UU. (PE / Crédito Privado)\n"
        dosier += "• *Forbion Capital Fund I:* Europa / Países Bajos (Biotech)\n"
        dosier += "• *DFJ Esprit II:* Europa / Reino Unido (Tech VC)\n"
        dosier += "• *India Advantage Fund I:* Asia / India (Emerging Markets)\n\n"

        dosier += "📊 *CONCENTRACIÓN GEOGRÁFICA DE COMPRAS SECUNDARIAS*\n"
        dosier += "• *Canadá:* 8 Fondos (47.06% — T2C2, Skypoint, GTI V, Capimont)\n"
        dosier += "• *Estados Unidos:* 5 Fondos (29.41% — Apollo X, Woodside V, Entrepia)\n"
        dosier += "• *Europa:* 3 Fondos (17.65% — Forbion, DFJ Esprit, Human Health)\n"
        dosier += "• *Asia:* 1 Fondo (5.88% — India Advantage)\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Cartera secundaria de Coller asociada e integrada exitosamente.")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
