#!/usr/bin/env python3
import os
import sys
import time
from datetime import datetime

class M82MasterOrchestrator:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def run_pipeline(self):
        print(f"🚀 [M82 MOLINA HOLDINGS LLC] Iniciando ejecución máster — {self.timestamp}")
        print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")

        scripts = [
            ("m82_macro_engine.py", "1. Base de Datos Macro"),
            ("m82_macro_dosier.py", "2. Despacho Sovereign Macro Dosier"),
            ("m82_refinitiv_pipeline.py", "3. Indicadores & Calendario Refinitiv"),
            ("m82_credit_private_markets.py", "4. Credit Ratings Soberanos"),
            ("m82_private_markets.py", "5. Analytics PE Refinitiv & KKR")
        ]

        for script, description in scripts:
            print(f"\n⚡ Ejecutando: {description} ({script})...")
            if os.path.exists(script):
                exit_code = os.system(f"python {script}")
                if exit_code == 0:
                    print(f"  └── ✅ {script} completado.")
                else:
                    print(f"  └── ❌ Error en {script} (Código: {exit_code}).")
            else:
                print(f"  └── ⚠️ Archivo {script} no encontrado.")
            time.sleep(1)

        print("\n🏛️ [M82 COMPLETE] Suite sovereign completamente ejecutada.")

if __name__ == "__main__":
    M82MasterOrchestrator().run_pipeline()
