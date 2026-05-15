import time

def header():
    print("\033[1;33m" + "!"*60)
    print("   M82 LOGISTICS MONITOR: PANAMA CANAL vs. ENERGY GRID")
    print("   REF: REUTERS ID nL1N41S0MX")
    print("!"*60 + "\033[0m")

def analyze_bottleneck():
    print("[*] Analizando rutas: Suez (Conflict) | Panama (Drought Risk)...")
    time.sleep(1)
    risk_factor = 7.5 # Incremento por conflicto en Irán
    print(f"[!] Alerta de Suministro: Demanda de Gas en ascenso por desvío de buques.")
    print(f"[+] Oportunidad Molina: Generación Local On-Site para reducir dependencia de fletes.")

header()
analyze_bottleneck()
