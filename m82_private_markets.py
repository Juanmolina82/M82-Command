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

    def parse_fund_summary(self):
        fund_info = {
            "Fund Name": "KKR North America Fund XIV SCSp",
            "Management Firm": "Kohlberg Kravis Roberts & Co LP",
            "Vintage Year": 2024,
            "Fund Stage": "Generalist",
            "Fund Size": "23,000.00M USD",
            "Status": "Had Final Close"
        }
        
        top_funds = [
            {"Fund": "KKR North America Fund XIV SCSp", "Size (M USD)": 23000.00, "Stage": "Generalist", "Vintage": 2024},
            {"Fund": "KKR Global Infrastructure Investors V", "Size (M USD)": 19200.00, "Stage": "Buyouts", "Vintage": 2023},
            {"Fund": "KKR North America Fund XIII SCSp", "Size (M USD)": 19000.00, "Stage": "Buyouts", "Vintage": 2020},
            {"Fund": "KKR 2006 Fund Private Investors, LLC", "Size (M USD)": 17600.00, "Stage": "Buyouts", "Vintage": 2006},
            {"Fund": "KKR Global Infrastructure Investors IV SCSp", "Size (M USD)": 17000.00, "Stage": "Buyouts", "Vintage": 2021},
        ]
        return fund_info, pd.DataFrame(top_funds)

    def parse_market_overview(self):
        stage_breakdown = [
            {"Stage": "Generalist", "Amount (M USD)": 212795.39, "Share": "34.1%"},
            {"Stage": "Buyouts", "Amount (M USD)": 182279.47, "Share": "29.2%"},
            {"Stage": "Balanced Stage", "Amount (M USD)": 65388.72, "Share": "10.5%"},
            {"Stage": "Secondary Funds", "Amount (M USD)": 32895.87, "Share": "5.3%"},
            {"Stage": "Early Stage", "Amount (M USD)": 25800.49, "Share": "4.1%"},
            {"Stage": "Otros (Opportunistic, Value Add, Core, Mezzanine)", "Amount (M USD)": 82093.41, "Share": "16.8%"},
        ]
        return pd.DataFrame(stage_breakdown)

    def dispatch(self):
        fund_info, df_funds = self.parse_fund_summary()
        df_stages = self.parse_market_overview()

        dosier = "💼 *[M82 PRIVATE MARKETS INTELLIGENCE — MOLINA HOLDINGS LLC]* 💼\n"
        dosier += f"🕒 *Sincronización Refinitiv:* `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"

        dosier += f"🏛️ *FONDO DESTACADO: {fund_info['Fund Name']}*\n"
        dosier += f"• *Firma Gestora:* {fund_info['Management Firm']}\n"
        dosier += f"• *Tamaño:* `{fund_info['Fund Size']}` | *Vintage:* `{fund_info['Vintage Year']}`\n"
        dosier += f"• *Estatus:* {fund_info['Status']} ({fund_info['Fund Stage']})\n\n"

        dosier += "📊 *TOP FONDOS GESTIONADOS POR LA FIRMA*\n"
        for _, row in df_funds.iterrows():
            dosier += f"• *{row['Fund']}* ({row['Vintage']}): `${row['Size (M USD)']:,.2f}M USD` — `{row['Stage']}`\n"

        dosier += "\n🌐 *DESGLOSE DE MERCADO POR FUND STAGE (REFINITIV PE)*\n"
        for _, row in df_stages.iterrows():
            dosier += f"• *{row['Stage']}*: `${row['Amount (M USD)']:,.2f}M USD` ({row['Share']})\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("✅ M82 Private Markets Intelligence despachado con éxito.")
            else:
                print(f"❌ Error al enviar a Telegram: {res.text}")
        except Exception as e:
            print(f"⚠️ Fallo de conexión: {e}")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
