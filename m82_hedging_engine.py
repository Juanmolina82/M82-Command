#!/usr/bin/env python3
import pandas as pd

def calculate_collar_structure():
    production_bbl_per_month = 45000  # Cobertura sobre ~1,500 bpd
    months = 24
    total_hedged_volume = production_bbl_per_month * months
    
    put_strike = 65.0
    call_strike = 88.5
    base_price = 75.0
    
    print("🛡️ --- ESTRUCTURA DE COBERTURA ZERO-COST COLLAR (M82 ENERGY) ---")
    print(f"• Volumen Cubierto (70% P1 Production, 24M): {total_hedged_volume:,.0f} bbls")
    print(f"• Piso Garantizado (Put Option): ${put_strike:.2f} / bbl")
    print(f"• Techo Cap (Call Option): ${call_strike:.2f} / bbl")
    print(f"• Costo Neto de Prima (Net Outlay): $0.00 USD\n")
    
    scenarios = [50, 60, 65, 75, 85, 95]
    summary = []
    
    for spot in scenarios:
        if spot < put_strike:
            effective_price = put_strike
            status = "Put Exercised (Floor Protected)"
        elif spot > call_strike:
            effective_price = call_strike
            status = "Call Exercised (Capped)"
        else:
            effective_price = spot
            status = "Unhedged Spot Realization"
            
        realized_revenue = effective_price * total_hedged_volume
        summary.append({
            "Spot_Brent": f"${spot}.00",
            "Effective_Price": f"${effective_price:.2f}",
            "24M_Realized_Revenue": f"${realized_revenue/1e6:.2f}M USD",
            "Status": status
        })
        
    df = pd.DataFrame(summary)
    print(df.to_string(index=False))

if __name__ == "__main__":
    calculate_collar_structure()
