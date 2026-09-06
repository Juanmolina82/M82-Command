#!/usr/bin/env python3
import os
import requests
import pandas as pd
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"  # @MOLINAHOLDINGS

class M82AdvancedRefinitivEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def parse_credit_ratings_and_sovereign_reviews(self):
        ratings_data = [
            {"Date": "4 Sep", "Agency": "S&P", "Entity": "United Arab Emirates", "Type": "Sovereign Rating Review"},
            {"Date": "4 Sep", "Agency": "DBRS", "Entity": "Hellenic Republic (Greece)", "Type": "Sovereign Rating Review"},
            {"Date": "4 Sep", "Agency": "Fitch", "Entity": "Portugal", "Type": "Sovereign Rating Review"},
            {"Date": "4 Sep", "Agency": "Fitch", "Entity": "Qatar", "Type": "Sovereign Rating Review"},
            {"Date": "4 Sep", "Agency": "S&P", "Entity": "Ukraine", "Type": "Sovereign Rating Review"},
            {"Date": "4 Sep", "Agency": "S&P", "Entity": "Ethiopia", "Type": "Sovereign Rating Review"},
            {"Date": "4 Sep", "Agency": "DBRS", "Entity": "Cyprus", "Type": "Sovereign Rating Review"},
            {"Date": "4 Sep", "Agency": "S&P", "Entity": "Iceland", "Type": "Sovereign Rating Review"},
        ]
        return pd.DataFrame(ratings_data)

    def generate_sovereign_prompts(self):
        return [
            "📌 *Prompt S&P / Fitch Ratings:* 'M82: Extrae los cambios de outlook y calificación para los soberanos revisados el 4 de Septiembre y analiza su impacto en spreads de deuda externa.'",
            "📌 *Prompt Private Markets / Cambridge PE:* 'M82: Cruza los datos de valoración de la cartera Incover contra el mPME (Public Market Equivalent) para ajustar el NAV de Q3.'",
            "📌 *Prompt Macro Surprise Index:* 'M82: Calcula el delta de sorpresa entre la encuesta Reuters Poll y el dato oficial para los datos de balanza comercial en Asia Pacific.'"
        ]

    def dispatch(self):
        df_ratings = self.parse_credit_ratings_and_sovereign_reviews()
        prompts = self.generate_sovereign_prompts()

        dosier = "🏛️ *[M82 ADVANCED CREDIT & PRIVATE MARKETS — MOLINA HOLDINGS LLC]* 🏛️\n"
        dosier += f"🕒 *Sincronización M82:* `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"

        dosier += "🏷️ *REVISIONES DE RATINGS SOBERANOS (REFINITIV WORKSPACE)*\n"
        for _, row in df_ratings.iterrows():
            dosier += f"• *[{row['Date']}] {row['Agency']}* | {row['Entity']} — `{row['Type']}`\n"

        dosier += "\n🤖 *PROMPTS OPERATIVOS M82 CONSOLE*\n"
        for p in prompts:
            dosier += f"{p}\n\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("✅ M82 Credit & Private Markets Intelligence despachado.")
            else:
                print(f"❌ Error al enviar: {res.text}")
        except Exception as e:
            print(f"⚠️ Fallo de conexión: {e}")

if __name__ == "__main__":
    M82AdvancedRefinitivEngine().dispatch()
