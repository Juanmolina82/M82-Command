#!/usr/bin/env python3
import pandas as pd
import numpy as np

def generate_upstream_sensitivity():
    # Parámetros base del activo
    base_nav = 150.0  # Millions USD
    brent_prices = [65, 75, 85]
    wacc_rates = [0.10, 0.12, 0.15]
    
    # Elasticidad aproximada del flujo operando: +/- 1.9x por cada $10/bbl
    # Factor de descuento ajustado por plazo medio de reservas (P1/P2)
    
    results = {}
    for brent in brent_prices:
        col_name = f"Brent_${brent}"
        results[col_name] = []
        for rate in wacc_rates:
            # Factor de ajuste respecto a escenario base ($75 Brent @ 12% WACC)
            price_delta = (brent - 75) * 2.65
            wacc_impact = (0.12 - rate) * 115.0
            val = base_nav + price_delta + wacc_impact
            results[col_name].append(round(val, 1))

    df = pd.DataFrame(results, index=["WACC_10%", "WACC_12%", "WACC_15%"])
    
    print("\n🛢️ --- MATRIZ DE SENSIBILIDAD IFRS 13 LEVEL 3 (M82 ENERGY ASSET CORP) ---")
    print("Valores expresados en Millones de USD ($M):\n")
    print(df)
    return df

if __name__ == "__main__":
    generate_upstream_sensitivity()
