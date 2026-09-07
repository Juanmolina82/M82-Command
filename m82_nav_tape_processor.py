#!/usr/bin/env python3
import os
import pandas as pd
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

class M82InstitutionalNAVEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def execute_audit(self):
        # Datos de portafolio ajustados a la realidad institucional
        portfolio = [
            {
                "Vehicle": "Coller International Partners VIII (LP Interest)",
                "GP_Total_AUM": "USD 9.15B (Fund Size)",
                "Strategy": "Global Private Equity Secondary",
                "M82_Commitment_NAV": 450000000,
                "GP_NAV_Discount": 0.12,  # 12% Descuento Secondary de entrada
                "DPI": 0.65,
                "TVPI": 1.78,
                "Lifecycle": "Harvest Phase (Vintage 2021)"
            },
            {
                "Vehicle": "Coller Secondary Energy & Transition Portfolio",
                "GP_Total_AUM": "Co-Investment / Direct Secondary",
                "Strategy": "Energy Transition Infrastructure",
                "M82_Commitment_NAV": 280000000,
                "GP_NAV_Discount": 0.18,  # 18% Descuento Secondary
                "DPI": 0.12,
                "TVPI": 1.25,
                "Lifecycle": "Deployment / J-Curve Phase"
            },
            {
                "Vehicle": "M82 Energy Asset Corp (Direct Operating)",
                "GP_Total_AUM": "USD 150M (Direct Asset)",
                "Strategy": "Upstream O&G Real Assets",
                "M82_Commitment_NAV": 150000000,
                "GP_NAV_Discount": 0.00,  # Activo directo (DCF IFRS 13 Level 3)
                "DPI": 0.85,
                "TVPI": 2.10,
                "Lifecycle": "Mature Cash Generator"
            }
        ]

        df = pd.DataFrame(portfolio)
        
        # Cálculo de NAV Ajustado por Descuento IFRS 13 Level 3
        df["Adjusted_IFRS13_NAV"] = df["M82_Commitment_NAV"] * (1 - df["GP_NAV_Discount"])
        
        total_reported_nav = df["M82_Commitment_NAV"].sum()
        total_adjusted_nav = df["Adjusted_IFRS13_NAV"].sum()

        dosier = "📊 *[M82 INSTITUTIONAL NAV AUDIT - IFRS 13 LEVEL 3]* 📊\n"
        dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
        
        dosier += f"💼 *LP Reported NAV Exposure:* `${total_reported_nav:,.2f} USD`\n"
        dosier += f"🛡️ *IFRS 13 Adjusted NAV (Secondary Disc.):* `${total_adjusted_nav:,.2f} USD`\n\n"
        dosier += "📋 *DESGLOSE DE PORTAFOLIO Y CICLO DE VIDA:*\n\n"

        for _, row in df.iterrows():
            dosier += f"• *{row['Vehicle']}*\n"
            dosier += f"  - Contexto GP: `{row['GP_Total_AUM']}`\n"
            dosier += f"  - Estrategia: `{row['Strategy']}`\n"
            dosier += f"  - NAV Reportado LP: `${row['M82_Commitment_NAV']:,.2f}`\n"
            dosier += f"  - Descuento Entrada/Level 3: `{row['GP_NAV_Discount']*100:.1f}%` $\rightarrow$ Adj NAV: `${row['Adjusted_IFRS13_NAV']:,.2f}`\n"
            dosier += f"  - Métricas: DPI `{row['DPI']}x` | TVPI `{row['TVPI']}x`\n"
            dosier += f"  - Estado: `{row['Lifecycle']}`\n\n"

        dosier += "✅ *Estatus Audit:* Claridad de AUM GP vs LP establecida. Descuentos Level 3 aplicados."

        print(dosier)
        self._dispatch(dosier)

    def _dispatch(self, message):
        if not TOKEN or not CHAT_ID:
            print("⚠️ Error: Credenciales no detectadas en .env")
            return

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("\n✅ Reporte institucional limpio y transmitido exitosamente.")
        except Exception as e:
            print(f"❌ Error de conexión: {e}")

if __name__ == "__main__":
    M82InstitutionalNAVEngine().execute_audit()
