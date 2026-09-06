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

    def parse_market_overview(self):
        total_raised_usd = 657820.29
        total_funds_count = 1682
        
        stages = [
            {"Stage": "Generalist", "Raised_M": 212795.39, "Funds": 355},
            {"Stage": "Buyouts", "Raised_M": 182279.47, "Funds": 209},
            {"Stage": "Balanced Stage", "Raised_M": 65388.72, "Funds": 592},
            {"Stage": "Secondary Funds", "Raised_M": 32895.87, "Funds": 12},
            {"Stage": "Early Stage", "Raised_M": 25800.49, "Funds": 202},
        ]
        
        locations = [
            {"Country": "United States", "Raised_M": 480172.79, "Funds": 1245},
            {"Country": "United Kingdom", "Raised_M": 50043.57, "Funds": 70},
            {"Country": "Luxembourg", "Raised_M": 30388.58, "Funds": 34},
            {"Country": "Hong Kong", "Raised_M": 14788.26, "Funds": 4},
            {"Country": "Netherlands", "Raised_M": 13903.42, "Funds": 15},
        ]
        return total_raised_usd, total_funds_count, pd.DataFrame(stages), pd.DataFrame(locations)

    def dispatch(self):
        total_amt, total_cnt, df_stages, df_locs = self.parse_market_overview()

        dosier = "📊 *[M82 PRIVATE MARKETS — GLOBAL OVERVIEW]* 📊\n"
        dosier += f"🏛️ *Molina Holdings LLC Intelligence* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"

        dosier += f"🌐 *TOTAL CAPITAL GLOBAL RECAUDADO*\n"
        dosier += f"• *Monto Total:* `${total_amt:,.2f}M USD`\n"
        dosier += f"• *Fondos Activos:* `{total_cnt:,}` fondos\n\n"

        dosier += "📈 *TOP ESTRATEGIAS (FUND STAGE)*\n"
        for _, r in df_stages.iterrows():
            pct = (r['Raised_M'] / total_amt) * 100
            dosier += f"• *{r['Stage']}*: `${r['Raised_M']:,.2f}M USD` ({pct:.1f}%) | `{r['Funds']}` fondos\n"

        dosier += "\n🌍 *TOP GEOGRAFÍAS (FUND LOCATION)*\n"
        for _, r in df_locs.iterrows():
            pct = (r['Raised_M'] / total_amt) * 100
            dosier += f"• *{r['Country']}*: `${r['Raised_M']:,.2f}M USD` ({pct:.1f}%) | `{r['Funds']}` fondos\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("✅ Reporte de Private Markets Overview enviado a Telegram.")
            else:
                print(f"❌ Error enviando a Telegram: {res.text}")
        except Exception as e:
            print(f"⚠️ Error de conexión: {e}")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
