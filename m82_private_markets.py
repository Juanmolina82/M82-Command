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

    def parse_largest_funds(self):
        largest_funds = [
            {"Fund Name": "General Atlantic Partners (Bermuda) IV LP", "Size (M USD)": 23701.01},
            {"Fund Name": "KKR North America Fund XIV SCSp", "Size (M USD)": 23000.00},
            {"Fund Name": "Francisco Partners VIII, L.P.", "Size (M USD)": 23000.00},
            {"Fund Name": "Sequoia Capital Fund LP", "Size (M USD)": 22722.25},
            {"Fund Name": "KKR Global Infrastructure Investors V", "Size (M USD)": 19200.00},
            {"Fund Name": "Coller International Partners IX", "Size (M USD)": 17000.00},
            {"Fund Name": "BPEA Private Equity Fund IX", "Size (M USD)": 15600.00},
            {"Fund Name": "Veritas Capital Fund IX LP", "Size (M USD)": 15300.00},
            {"Fund Name": "Clearlake Capital Partners VIII, LP", "Size (M USD)": 14800.00},
            {"Fund Name": "Blackstone Capital Partners Asia III LP", "Size (M USD)": 13100.00},
        ]
        return pd.DataFrame(largest_funds), 187423.25

    def parse_featured_funds(self):
        # Datos extraídos de los reportes oficiales Refinitiv (VEID: 627364 y 624496)
        fp_fund = {
            "Fund Name": "Francisco Partners VIII, L.P.",
            "VEID": "627364",
            "Firm": "Francisco Partners LP",
            "Size": "23,000.00M USD",
            "Vintage": 2026,
            "Stage": "All Buyouts"
        }
        coller_fund = {
            "Fund Name": "Coller International Partners IX",
            "VEID": "624496",
            "Firm": "Coller Capital Ltd",
            "Size": "17,000.00M USD",
            "Vintage": 2026,
            "Stage": "Secondary Funds"
        }
        return fp_fund, coller_fund

    def dispatch(self):
        df_funds, total_raised = self.parse_largest_funds()
        fp_fund, coller_fund = self.parse_featured_funds()

        dosier = "💼 *[M82 PRIVATE MARKETS — REFINITIV INTELLIGENCE]* 💼\n"
        dosier += f"🏛️ *Molina Holdings LLC Intelligence* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"

        dosier += "🏛️ *FONDOS DESTACADOS REVISADOS*\n"
        dosier += f"• *{fp_fund['Fund Name']}* (VEID: {fp_fund['VEID']})\n"
        dosier += f"  Gestor: {fp_fund['Firm']} | Tamaño: `{fp_fund['Size']}` | Estrategia: {fp_fund['Stage']}\n\n"
        dosier += f"• *{coller_fund['Fund Name']}* (VEID: {coller_fund['VEID']})\n"
        dosier += f"  Gestor: {coller_fund['Firm']} | Tamaño: `{coller_fund['Size']}` | Estrategia: {coller_fund['Stage']}\n\n"

        dosier += "🌐 *TOP 10 FONDOS MÁS GRANDES LEVANTADOS*\n"
        for idx, row in df_funds.iterrows():
            dosier += f"{idx+1}. *{row['Fund Name']}*: `${row['Size (M USD)']:,.2f}M USD`\n"

        dosier += f"\n📊 *Total Acumulado Top 10:* `${total_raised:,.2f}M USD`\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("✅ M82 Private Markets actualizado y despachado a Telegram.")
            else:
                print(f"❌ Error al enviar a Telegram: {res.text}")
        except Exception as e:
            print(f"⚠️ Fallo de conexión: {e}")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
