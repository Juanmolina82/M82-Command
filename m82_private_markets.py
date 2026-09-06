#!/usr/bin/env python3
import os
import requests
import pandas as pd
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"  # @MOLINAHOLDINGS

class M82PrivateMarketsEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def parse_coller_details(self):
        coller_fund = {
            "Fund Name": "Coller International Partners IX",
            "VEID": "624496",
            "Firm": "Coller Capital Ltd",
            "Address": "116 Park Street, Park House, London W1GK 6AF, UK",
            "Size": "17,000.00M USD",
            "Vintage": 2026,
            "Stage": "Secondary Funds / Fund Of Funds",
            "Status": "Had Final Close",
            "CIO": "Jeremy Coller"
        }
        
        history = [
            {"Fund": "Coller International Partners IX", "Size (M USD)": 17000.00, "Vintage": 2026},
            {"Fund": "Coller International Partners VIII", "Size (M USD)": 9000.00, "Vintage": 2020},
            {"Fund": "Coller International Partners VII", "Size (M USD)": 7150.00, "Vintage": 2015},
            {"Fund": "Coller International Partners VI, L.P.", "Size (M USD)": 5500.00, "Vintage": 2012},
            {"Fund": "Coller International Partners V", "Size (M USD)": 4800.00, "Vintage": 2006},
            {"Fund": "Coller International Partners IV, L.P.", "Size (M USD)": 2600.00, "Vintage": 2002},
        ]
        return coller_fund, pd.DataFrame(history)

    def dispatch(self):
        coller_fund, df_history = self.parse_coller_details()

        dosier = "💼 *[M82 PRIVATE MARKETS — REFINITIV FUND SUMMARY]* 💼\n"
        dosier += f"🏛️ *Molina Holdings LLC Intelligence* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"

        dosier += f"🏛️ *FONDO: {coller_fund['Fund Name']} (VEID: {coller_fund['VEID']})*\n"
        dosier += f"• *Gestora:* {coller_fund['Firm']}\n"
        dosier += f"• *Ubicación:* {coller_fund['Address']}\n"
        dosier += f"• *Tamaño Final:* `{coller_fund['Size']}`\n"
        dosier += f"• *Estatus:* {coller_fund['Status']} | *Vintage:* `{coller_fund['Vintage']}`\n"
        dosier += f"• *Estrategia:* {coller_fund['Stage']}\n"
        dosier += f"• *CIO / Liderazgo:* {coller_fund['CIO']}\n\n"

        dosier += "📊 *HISTÓRICO DE FONDOS COLLER CAPITAL*\n"
        for _, row in df_history.iterrows():
            dosier += f"• *{row['Fund']}* ({row['Vintage']}): `${row['Size (M USD)']:,.2f}M USD`\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("✅ Ficha de Coller International Partners IX enviada a Telegram.")
            else:
                print(f"❌ Error al enviar a Telegram: {res.text}")
        except Exception as e:
            print(f"⚠️ Fallo de conexión: {e}")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
