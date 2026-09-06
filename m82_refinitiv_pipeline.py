#!/usr/bin/env python3
import os
import requests
import pandas as pd
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"  # @MOLINAHOLDINGS

class M82RefinitivEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def parse_economic_events(self):
        # Datos del Monitor de Indicadores Económicos (Refinitiv Workspace)
        economic_data = [
            {"Country": "🇦🇺 AU", "Indicator": "S&P Global Mfg PMI Final", "Period": "Aug", "Actual": "52.0", "Surprise": "-"},
            {"Country": "🇯🇵 JP", "Indicator": "Business Capex (MOF) YY", "Period": "Q2", "Actual": "1.6%", "Surprise": "-"},
            {"Country": "🇰🇷 KR", "Indicator": "Export Growth Prelim", "Period": "Aug", "Actual": "68.7%", "Surprise": "+6.10%"},
            {"Country": "🇰🇷 KR", "Indicator": "Trade Balance Prelim", "Period": "Aug", "Actual": "34.75B", "Surprise": "+4.01B"},
            {"Country": "🇮🇪 IE", "Indicator": "PMI Manufacturing", "Period": "Aug", "Actual": "55.4", "Surprise": "-"},
            {"Country": "🇯🇵 JP", "Indicator": "S&P Global Mfg PMI Final", "Period": "Aug", "Actual": "54.9", "Surprise": "-"},
            {"Country": "🇮🇩 ID", "Indicator": "Inflation YY", "Period": "Aug", "Actual": "3.19%", "Surprise": "+0.06%"},
            {"Country": "🇮🇩 ID", "Indicator": "Core Inflation YY", "Period": "Aug", "Actual": "2.92%", "Surprise": "+0.12%"},
        ]
        return pd.DataFrame(economic_data)

    def parse_central_bank_events(self):
        # Datos del Calendario de Bancos Centrales y Geopolítica (Refinitiv Workspace)
        cb_data = [
            {"Date": "6 Sep", "Country": "🛢️ OPEC", "Event": "Reunión ministerial de 7 países OPEC+"},
            {"Date": "7 Sep", "Country": "🇪🇺 EU", "Event": "Discurso del Comisionado de Comercio de la UE Maros Sefcovic"},
            {"Date": "8 Sep", "Country": "🇺🇸 US", "Event": "Reserva Federal publica datos de Crédito al Consumidor"},
            {"Date": "8 Sep", "Country": "🇨🇱 CL", "Event": "Reunión de Política Monetaria del Banco Central de Chile"},
            {"Date": "9 Sep", "Country": "🇪🇺 ECB", "Event": "Reunión del Consejo de Gobierno del BCE"},
            {"Date": "9 Sep", "Country": "🇦🇷 AR", "Event": "Banco Central de Argentina publica REM mensual"},
        ]
        return pd.DataFrame(cb_data)

    def dispatch(self):
        df_econ = self.parse_economic_events()
        df_cb = self.parse_central_bank_events()

        dosier = "🏛️ *[M82 REFINITIV INTELLIGENCE — MOLINA HOLDINGS LLC]* 🏛️\n"
        dosier += f"🕒 *Sincronización:* `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"

        dosier += "📈 *INDICADORES MACRO CLAVE (REFINITIV WORKSPACE)*\n"
        for _, row in df_econ.iterrows():
            surp = f" (Sorpresa: `{row['Surprise']}`)" if row['Surprise'] != '-' else ""
            dosier += f"• *{row['Country']}* | {row['Indicator']} ({row['Period']}): *{row['Actual']}*{surp}\n"

        dosier += "\n🏛️ *CALENDARIO DE BANCOS CENTRALES Y EVENTOS POLÍTICOS*\n"
        for _, row in df_cb.iterrows():
            dosier += f"• *[{row['Date']}] {row['Country']}*: {row['Event']}\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("✅ Refinitiv Intelligence enviado con éxito a Telegram.")
            else:
                print(f"❌ Error al enviar: {res.text}")
        except Exception as e:
            print(f"⚠️ Fallo de conexión: {e}")

if __name__ == "__main__":
    M82RefinitivEngine().dispatch()
