#!/usr/bin/env python3
import requests
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"

class M82CreditAnalyticsEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def dispatch(self):
        dosier = "🛡️ *[M82 CREDIT ANALYTICS — COLLER CAPITAL LTD]* 🛡️\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "⭐ *RATING CREDITICIO:* `AAA` (PoD: 0.02%)\n\n"
        
        dosier += "📊 *DESGLOSE DE SCORES DE CRÉDITO*\n"
        dosier += "• *Profitability (82/100):* ROTC 27.60% | Net Margin 4.25%\n"
        dosier += "• *Coverage (100/100):* Cobertura Total de Intereses\n"
        dosier += "• *Leverage (100/100):* Debt/Assets 0.01 | Net Debt/Equity -0.42\n"
        dosier += "• *Liquidity (50/100):* Cash/Debt 2.58x | Quick Ratio 1.42x\n"
        dosier += "• *Growth & Stability (33/100):* ROE StdDev 2.50\n\n"

        dosier += "💡 *VALORACIÓN ESTRATÉGICA:* Excelente salud financiera estructural, riesgo de impago prácticamente nulo y solidez de caja neta superior al promedio del sector."

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Perfil de crédito AAA de Coller Capital enviado a Telegram.")

if __name__ == "__main__":
    M82CreditAnalyticsEngine().dispatch()
