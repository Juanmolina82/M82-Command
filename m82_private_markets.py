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

    def parse_francisco_partners_details(self):
        fp_fund = {
            "Fund Name": "Francisco Partners VIII, L.P.",
            "VEID": "627364",
            "Management Firm": "Francisco Partners LP",
            "Fund Size": "23,000.00M USD",
            "Target Size": "14,000.00M USD",
            "Vintage Year": 2026,
            "Fund Stage": "All Buyouts",
            "Status": "Had Final Close"
        }
        
        historical_funds = [
            {"Fund": "Francisco Partners VIII, L.P.", "Size (M USD)": 23000.00, "Vintage": 2026},
            {"Fund": "FRANCISCO PARTNERS VII, L.P.", "Size (M USD)": 13500.00, "Vintage": 2022},
            {"Fund": "Francisco Partners VI LP", "Size (M USD)": 7450.00, "Vintage": 2020},
            {"Fund": "Francisco Partners V", "Size (M USD)": 3975.00, "Vintage": 2017},
            {"Fund": "FRANCISCO PARTNERS AGILITY III, L.P.", "Size (M USD)": 3300.00, "Vintage": 2022},
            {"Fund": "FP Credit Partners III, L.P.", "Size (M USD)": 3300.00, "Vintage": 2025},
        ]
        return fp_fund, pd.DataFrame(historical_funds)

    def dispatch(self):
        df_funds, total_raised = self.parse_largest_funds()
        fp_fund, df_fp_history = self.parse_francisco_partners_details()

        dosier = "💼 *[M82 PRIVATE MARKETS & FUND SUMMARY — REFINITIV]* 💼\n"
        dosier += f"🏛️ *Molina Holdings LLC Intelligence* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"

        dosier += f"🏛️ *FONDO DESTACADO: {fp_fund['Fund Name']} (VEID: {fp_fund['VEID']})*\n"
        dosier += f"• *Firma Gestora:* {fp_fund['Management Firm']}\n"
        dosier += f"• *Tamaño Final:* `{fp_fund['Fund Size']}` | *Objetivo:* `{fp_fund['Target Size']}`\n"
        dosier += f"• *Estatus:* {fp_fund['Status']} | *Vintage:* `{fp_fund['Vintage Year']}`\n"
        dosier += f"• *Estrategia:* {fp_fund['Fund Stage']}\n\n"

        dosier += "📊 *HISTÓRICO PRINCIPALES FONDOS FRANCISCO PARTNERS*\n"
        for _, row in df_fp_history.iterrows():
            dosier += f"• *{row['Fund']}* ({row['Vintage']}): `${row['Size (M USD)']:,.2f}M USD`\n"

        dosier += "\n🌐 *TOP 10 FONDOS MÁS GRANDES LEVANTADOS (GLOBAL)*\n"
        for idx, row in df_funds.iterrows():
            dosier += f"{idx+1}. *{row['Fund Name']}*: `${row['Size (M USD)']:,.2f}M USD`\n"

        dosier += f"\n📊 *Total Acumulado Top 10:* `${total_raised:,.2f}M USD`\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("✅ M82 Private Markets despachado a Telegram con éxito.")
            else:
                print(f"❌ Error al enviar a Telegram: {res.text}")
        except Exception as e:
            print(f"⚠️ Fallo de conexión: {e}")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
