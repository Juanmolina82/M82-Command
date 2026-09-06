#!/usr/bin/env python3
import os
import requests
import pandas as pd
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"  # @MOLINAHOLDINGS

class M82IntradayAlertEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def check_intraday_alerts(self):
        alerts = [
            {"Asset": "FX / USD-CLP", "Condition": "Breach +1.5%", "Level": "948.50", "Severity": "🔴 HIGH"},
            {"Asset": "Bonds / US 10Y Yield", "Condition": "Spike > 4.25%", "Level": "4.28%", "Severity": "🟡 MEDIUM"},
        ]
        return pd.DataFrame(alerts)

    def dispatch(self):
        df_alerts = self.check_intraday_alerts()

        dosier = "🚨 *[M82 INTRADAY MARKET ALERT — MOLINA HOLDINGS LLC]* 🚨\n"
        dosier += f"🕒 *Timestamp:* `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"

        for _, row in df_alerts.iterrows():
            dosier += f"• *{row['Severity']}* | *{row['Asset']}*: `{row['Level']}` ({row['Condition']})\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("✅ Alerta intradía despachada correctamente.")
            else:
                print(f"❌ Error al enviar alerta: {res.text}")
        except Exception as e:
            print(f"⚠️ Fallo de conexión: {e}")

if __name__ == "__main__":
    M82IntradayAlertEngine().dispatch()
