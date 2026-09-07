#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class M82InstitutionalNAVProcessor:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def run_pipeline(self):
        # 1. Base Portfolio Exposure
        portfolio_data = [
            {
                "Vehicle": "Coller International Partners VIII (LP Interest)",
                "Strategy": "Global Private Equity Secondary",
                "Reported_NAV": 450.0,
                "IFRS13_Discount": 0.12,
                "Base_NAV": 396.0
            },
            {
                "Vehicle": "Coller Secondary Energy & Transition",
                "Strategy": "Energy Transition Infra Secondary",
                "Reported_NAV": 280.0,
                "IFRS13_Discount": 0.18,
                "Base_NAV": 229.6
            },
            {
                "Vehicle": "M82 Energy Asset Corp (Direct Upstream)",
                "Strategy": "Upstream O&G Real Assets",
                "Reported_NAV": 150.0,
                "IFRS13_Discount": 0.00,
                "Base_NAV": 150.0
            }
        ]
        
        df = pd.DataFrame(portfolio_data)
        
        # 2. Escenarios IFRS 13 Level 3 DCF para M82 Energy Asset Corp
        upstream_base = 150.0
        upstream_stress = 126.6  # Brent $65 / WACC 15% (-15.6%)
        upstream_upside = 173.1  # Brent $85 / WACC 10% (+15.4%)
        
        fixed_secondaries_nav = df[df["Vehicle"] != "M82 Energy Asset Corp (Direct Upstream)"]["Base_NAV"].sum() # 625.6M
        
        total_nav_base = fixed_secondaries_nav + upstream_base     # $775.6M
        total_nav_stress = fixed_secondaries_nav + upstream_stress # $752.2M
        total_nav_upside = fixed_secondaries_nav + upstream_upside # $798.7M
        
        print("\n📊 --- SUMMARY DOSIER: MOLINA HOLDINGS LLC ---")
        print(f"• Total NAV Reportado LP: ${df['Reported_NAV'].sum():.1f}M USD")
        print(f"• Total NAV Ajustado Level 3 (Caso Base): ${total_nav_base:.1f}M USD")
        print(f"• Total NAV Ajustado Level 3 (Stress Down): ${total_nav_stress:.1f}M USD")
        print(f"• Total NAV Ajustado Level 3 (Upside): ${total_nav_upside:.1f}M USD\n")
        
        # 3. Generación del gráfico de sensibilidad
        self._generate_chart(upstream_stress, upstream_base, upstream_upside, 
                             total_nav_stress, total_nav_base, total_nav_upside)

    def _generate_chart(self, u_stress, u_base, u_upside, t_stress, t_base, t_upside):
        scenarios = ['Stress Down\n($65 / 15%)', 'Caso Base\n($75 / 12%)', 'Upside\n($85 / 10%)']
        m82_upstream = [u_stress, u_base, u_upside]
        total_nav = [t_stress, t_base, t_upside]

        x = np.arange(len(scenarios))
        width = 0.35

        fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
        rects1 = ax.bar(x - width/2, m82_upstream, width, label='M82 Energy Asset Corp ($M)', color='#2b6cb0')
        rects2 = ax.bar(x + width/2, total_nav, width, label='NAV Total Ajustado M82 ($M)', color='#0d2238')

        ax.set_ylabel('Valoración ($M USD)', fontsize=10, fontweight='bold')
        ax.set_title('Sensibilidad IFRS 13 Level 3 — M82 Energy Asset Corp & NAV Total', fontsize=12, fontweight='bold', pad=15)
        ax.set_xticks(x)
        ax.set_xticklabels(scenarios, fontsize=9, fontweight='bold')
        ax.legend(frameon=True, facecolor='#ffffff', edgecolor='#cbd5e0')
        ax.set_ylim(0, 900)

        for rect in rects1 + rects2:
            height = rect.get_height()
            ax.annotate(f'${height:.1f}M',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=8, fontweight='bold')

        plt.tight_layout()
        output_file = 'm82_sensitivity_chart.png'
        plt.savefig(output_file, dpi=300)
        print(f"📈 Gráfico institucional generado exitosamente: '{output_file}'")

if __name__ == "__main__":
    M82InstitutionalNAVProcessor().run_pipeline()
