#!/usr/bin/env python3
import os
import requests
import pandas as pd
from datetime import datetime

TOKEN = "8600412468:AAHLLRDPus66Y1hSgDKbwGC5zdW6DdufP3Y"
CHAT_ID = "1020305418"  # @MOLINAHOLDINGS

class M82PrivateMarketsEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def parse_coller_eqt_deal(self):
        coller_fund = {
            "Fund Name": "Coller International Partners IX",
            "VEID": "624496",
            "Firm": "Coller Capital Ltd (Subsidiary of EQT AB)",
            "Fund Size": "17,000.00M USD",
            "Corporate Deal": "Acquired by EQT AB for $3.2B USD",
            "Deal Status": "Closed / Combination Completed",
            "Vintage": 2026,
            "Stage": "Secondary Funds / Fund Of Funds",
            "CIO": "Jeremy Coller"
        }
        return coller_fund

    def dispatch(self):
        coller = self.parse_coller_eqt_deal()

        dosier = "💼 *[M82 PRIVATE MARKETS — REFINITIV CORPORATE DEAL]* 💼\n"
        dosier += f"🏛️ *Molina Holdings LLC Intelligence* | `{self.timestamp}`\n"
        dosier += "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n"

        dosier += f"🚨 *NOTICIA M&A: COMBINACIÓN EQT + COLLER CAPITAL*\n"
        dosier += f"• *Gestora Target:* Coller Capital Ltd\n"
        dosier += f"• *Comprador / Socio:* EQT AB (EQTAB.ST)\n"
        dosier += f"• *Valor de Transacción:* `$3,200.00M USD` ($3.2B)\n"
        dosier += f"• *Estatus M&A:* `{coller['Deal Status']}`\n\n"

        dosier += f"🏛️ *IMPACTO EN EL FONDO: {coller['Fund Name']} (VEID: {coller['VEID']})*\n"
        dosier += f"• *Tamaño del Fondo IX:* `{coller['Fund Size']}`\n"
        dosier += f"• *Estrategia:* {coller['Stage']}\n"
        dosier += f"• *Liderazgo Manteniéndose:* {coller['CIO']}\n"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": dosier, "parse_mode": "Markdown"}
        
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                print("✅ Evento EQT-Coller enviado exitosamente a Telegram.")
            else:
                print(f"❌ Error al enviar a Telegram: {res.text}")
        except Exception as e:
            print(f"⚠️ Error de conexión: {e}")

if __name__ == "__main__":
    M82PrivateMarketsEngine().dispatch()
