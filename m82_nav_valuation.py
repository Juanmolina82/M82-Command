#!/usr/bin/env python3
import requests
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"

class M82NAVValuationEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def dispatch(self):
        dosier = "📈 *[M82 NAV & VALUATION ASSESSMENT — COLLER LP CARTERA]* 📈\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += "📊 *ESTRUCTURA DE VALORACIÓN (FAIR VALUE)*\n"
        dosier += "• *Base Contable:* IFRS 13 / ASC 820 (Reportes GP trimestrales).\n"
        dosier += "• *Plataforma Coller AUM:* $50.00B USD a 2026.\n\n"

        dosier += "💵 *ESTIMACIÓN DE DESCUENTO ADQUIRIDO (ENTRY PRICING)*\n"
        dosier += "• *Apollo Fund X (Mega Buyout):* Comprado a ~92% del NAV.\n"
        dosier += "• *Forbion & BioTech (Europa):* Comprado a ~80% del NAV.\n"
        dosier += "• *DFJ Esprit & Tech VC:* Comprado a ~68% del NAV.\n"
        dosier += "• *Bloque Canadá (T2C2 / Skypoint / GTI):* Comprado a ~75% del NAV.\n\n"

        dosier += "🎯 *EFECTO CURVA J:* Mitigado. Entradas en valor positivo desde el Año 1 debido al descuento en la compra del secondary market."

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Integración de NAV y métricas financieras ejecutada correctamente.")

if __name__ == "__main__":
    M82NAVValuationEngine().dispatch()
