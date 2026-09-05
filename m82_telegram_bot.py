#!/usr/bin/env python3
import os
import requests
import pandas as pd

# Credenciales de Telegram
TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"

def dispatch_sovereign_alerts():
    excel_file = "Auctus_Coverage_and_News_2026.xlsx"
    
    if not os.path.exists(excel_file):
        print("❌ Error: 'Auctus_Coverage_and_News_2026.xlsx' no encontrado. Ejecuta 'm82_macro_engine.py' primero.")
        return

    df = pd.read_excel(excel_file, sheet_name="News & Updates")
    alerts = df[df['Category / Region'] == 'Auctus Publications']

    print(f"📡 Enviando {len(alerts)} alertas al Chat ID {CHAT_ID} (@MOLINAHOLDINGS)...")

    for _, row in alerts.iterrows():
        msg = (
            f"🚨 *[M82 SOVEREIGN ALERT]* 🚨\n\n"
            f"📌 *Empresa:* {row['Company']} ({row['Ticker']})\n"
            f"🎯 *Target Price:* `{row['Target Price / Offer']}`\n\n"
            f"📝 *Detalles:* {row['Key Highlights & Updates']}"
        )
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": msg,
            "parse_mode": "Markdown"
        }
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print(f"✅ Alerta enviada: {row['Company']}")
            else:
                print(f"❌ Error HTTP {res.status_code}: {res.text}")
        except Exception as e:
            print(f"⚠️ Fallo de conexión: {str(e)}")

if __name__ == "__main__":
    dispatch_sovereign_alerts()
