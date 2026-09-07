#!/usr/bin/env python3
import pandas as pd
import numpy as np

def execute_full_committee_pipeline():
    debt_facility = 150.0  # $150M USD
    max_ltv = 0.20        # 20.0% Max LTV
    
    # Matriz IFRS 13 Level 3
    scenarios = [
        {"Case": "Upside ($85 / 10%)", "Upstream_NAV": 173.1, "Total_NAV": 798.7},
        {"Case": "Caso Base ($75 / 12%)", "Upstream_NAV": 150.0, "Total_NAV": 775.6},
        {"Case": "Stress Down ($65 / 15%)", "Upstream_NAV": 126.6, "Total_NAV": 752.2}
    ]
    
    results = []
    for sc in scenarios:
        ltv = debt_facility / sc["Total_NAV"]
        headroom = (sc["Total_NAV"] * max_ltv) - debt_facility
        results.append({
            "Escenario": sc["Case"],
            "M82_Energy_NAV": f"${sc['Upstream_NAV']:.1f}M",
            "NAV_Total_Ajustado": f"${sc['Total_NAV']:.1f}M",
            "LTV_Resultante": f"{ltv*100:.2f}%",
            "Holgura_Covenant": f"${headroom:.2f}M USD",
            "Estatus": "COMPLIANT" if ltv < max_ltv else "BREACH"
        })
        
    df = pd.DataFrame(results)
    print("\n🏛️ --- DOSIER COMPLETO M82: SENSIBILIDAD IFRS 13 & TEST DE LTV ---")
    print(df.to_string(index=False))

if __name__ == "__main__":
    execute_full_committee_pipeline()
