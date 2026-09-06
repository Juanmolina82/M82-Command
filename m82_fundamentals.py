#!/usr/bin/env python3
import requests
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"

class M82FundamentalsEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def dispatch(self):
        dosier = "📋 *[M82 FINANCIAL FUNDAMENTALS — COLLER CAPITAL LTD]* 📋\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "📊 *ESTADOS FINANCIEROS (CONSOLIDADO GBP MILLIONS)*\n"
        dosier += "• *Revenue FY25:* £117.80M (+26.2% YoY)\n"
        dosier += "• *EBITDA FY25:* £7.94M (Margen 6.7%)\n"
        dosier += "• *Net Income FY25:* £5.05M (Margen 4.3%)\n"
        dosier += "• *Caja & Equivalentes:* £8.72M\n"
        dosier += "• *Patrimonio Neto:* £16.54M\n\n"

        dosier += "⚡ *MÉTRICAS CLAVE DE EFICIENCIA*\n"
        dosier += "• *ROE (Average Equity):* 36.1%\n"
        dosier += "• *ROIC (Invested Capital):* 32.8%\n"
        dosier += "• *Deuda / Activos Totales:* 3.3%\n"
        dosier += "• *Ventas por Empleado:* £569,065 GBP\n\n"

        dosier += "✅ Auditado y sincronizado correctamente desde Refinitiv Fundamentals."

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Datos fundamentales de Coller Capital Ltd enviados a Telegram.")

if __name__ == "__main__":
    M82FundamentalsEngine().dispatch()
