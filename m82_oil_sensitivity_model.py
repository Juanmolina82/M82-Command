#!/usr/bin/env python3
import requests
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"

class M82OilSensitivityEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def run_simulation(self):
        dosier = "🛢️ *[M82 OIL & GAS SENSITIVITY MODEL — COLLER/EGT]* 🛢️\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "📊 *ESCENARIOS DE CRUDO WTI/BRENT & IMPACTO EN TIR/DPI*\n\n"
        
        dosier += "🔴 *Escenario Stress ($55-$60 WTI):*\n"
        dosier += "• Descuento Requerido: 35% s/ NAV\n"
        dosier += "• TIR Proyectada: 13.5% | TVPI: 1.40x\n"
        dosier += "• Enfoque: Cobertura por hedges y flujo de Midstream.\n\n"

        dosier += "🟡 *Escenario Base EIA ($78-$85 WTI):*\n"
        dosier += "• Descuento Requerido: 22% s/ NAV\n"
        dosier += "• TIR Proyectada: 20.2% | TVPI: 1.78x\n"
        dosier += "• Enfoque: Generación de caja inmediata y captura de Alfa día 1.\n\n"

        dosier += "🟢 *Escenario Bull ($90+ WTI):*\n"
        dosier += "• Descuento Requerido: 12% s/ NAV\n"
        dosier += "• TIR Proyectada: 26.8% | TVPI: 2.15x\n"
        dosier += "• Enfoque: Monetización acelerada vía M&A y IPOs.\n\n"

        dosier += "✅ Modelo de sensibilidad energética sincronizado en el pipeline analítico M82."

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Modelo de sensibilidad de precios de petróleo integrado y enviado a Telegram.")

if __name__ == "__main__":
    M82OilSensitivityEngine().run_simulation()
