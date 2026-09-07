#!/usr/bin/env python3
import eikon as ek
import requests
from datetime import datetime

# --- CONFIGURACIÓN DE CREDENCIALES ---
# Sustituye 'TU_REFINITIV_APP_KEY' por la clave generada en tu App Key Generator de Refinitiv
REFINITIV_APP_KEY = "TU_REFINITIV_APP_KEY" 
TELEGRAM_TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"

class M82RefinitivRealTimeEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            ek.set_app_key(REFINITIV_APP_KEY)
            print("✅ Conexión establecida con Refinitiv Workspace / Eikon API.")
        except Exception as e:
            print(f"⚠️ Error de autenticación con la API de Refinitiv: {e}")

    def fetch_and_dispatch_commodities(self):
        # RICs de energía: WTI (CLc1), Brent (LCOc1), Gas Natural (NGc1)
        rics = ['CLc1', 'LCOc1', 'NGc1']
        fields = ['CF_LAST', 'CF_NETCHNG1', 'PCTCHNG']

        try:
            data, err = ek.get_data(rics, fields)
            
            dosier = "📊 *[M82 REAL-TIME COMMODITIES — REFINITIV API]* 📊\n"
            dosier += f"🏛️ *Molina Holdings LLC* | `{self.timestamp}`\n"
            dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"
            
            for index, row in data.iterrows():
                ric = row['Instrument']
                last = row['CF_LAST']
                chg = row['PCTCHNG']
                dosier += f"• *{ric}:* `${last:.2f}` USD (`{chg:+.2f}%`)\n"
                
            dosier += "\n⚡ *Status:* Transmisión en directo completada desde Refinitiv Workspace API."

        except Exception as e:
            dosier = f"⚠️ *Error al extraer datos en vivo de Refinitiv:* {e}\n"
            dosier += "Asegúrate de que la aplicación Refinitiv Workspace esté abierta en tu terminal o la API local esté activa."

        # Envío a Telegram
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            print("✅ Reporte en tiempo real transmitido con éxito a Telegram.")

if __name__ == "__main__":
    M82RefinitivRealTimeEngine().fetch_and_dispatch_commodities()
