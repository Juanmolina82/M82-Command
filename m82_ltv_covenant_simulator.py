#!/usr/bin/env python3
import pandas as pd

def run_ltv_simulation():
    facility_limit = 150.0  # $150M USD drawn
    max_ltv_covenant = 0.20 # 20%
    
    scenarios = [
        {"Name": "Upside ($85 / 10%)", "NAV": 798.7},
        {"Name": "Caso Base ($75 / 12%)", "NAV": 775.6},
        {"Name": "Stress Down ($65 / 15%)", "NAV": 752.2},
        {"Name": "Severe Stress ($55 / 18%)", "NAV": 720.0}
    ]
    
    table = []
    for sc in scenarios:
        ltv = (facility_limit / sc["NAV"])
        headroom = (sc["NAV"] * max_ltv_covenant) - facility_limit
        
        if ltv <= 0.18:
            status = "COMPLIANT (Safe)"
        elif ltv <= max_ltv_covenant:
            status = "WARNING (Near Threshold)"
        else:
            status = "BREACH (Cure Required)"
            
        table.append({
            "Scenario": sc["Name"],
            "Adjusted_NAV": f"${sc['NAV']}M",
            "Drawn_Debt": f"${facility_limit}M",
            "LTV_Ratio": f"{ltv*100:.2f}%",
            "Borrowing_Headroom": f"${headroom:.2f}M",
            "Covenant_Status": status
        })
        
    df = pd.DataFrame(table)
    print("\n🏦 --- SIMULACIÓN DE COVENANT LTV EN LÍNEA NAV ($150M) ---")
    print(df.to_string(index=False))

if __name__ == "__main__":
    run_ltv_simulation()
