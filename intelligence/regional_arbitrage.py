import time

def header():
    print("\033[1;32m" + "◈"*60)
    print("   M82 REGIONAL ARBITRAGE: COLOMBIA GDP vs. VENEZUELA RECOVERY")
    print("   DATA SOURCE: LSEG REUTERS nL1N41S0T2")
    print("◈"*60 + "\033[0m")

def compute_opportunity():
    col_gdp = 2.2
    col_rates = 11.25
    print(f"[*] Analizando Colombia: GDP {col_gdp}% | Tasas {col_rates}%")
    print("[!] Diagnóstico: Sector construcción en contracción. Saturación de mercado.")
    print("[→] Estrategia Molina: Posicionar Zulia como 'High-Yield Infrastructure' frente al estancamiento andino.")

header()
compute_opportunity()
