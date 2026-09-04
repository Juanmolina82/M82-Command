#!/usr/bin/env python3
import os
import shutil
import openpyxl
import pandas as pd

# ==========================================
# 1. BASE DE DATOS MÁSTER (Excel / Drive)
# ==========================================
def build_master_database():
    print("=== [1/3] Construyendo Base de Datos Máster ===")
    wb = openpyxl.Workbook()
    
    # Sheet 1: Metrics
    ws_metrics = wb.active
    ws_metrics.title = "Auctus Coverage Universe"
    ws_metrics.append(["Company", "Ticker", "Price Target", "Market Cap", "NAV", "Core NAV", "EV/DACF"])
    
    metrics = [
        ["ADX Energy", "ADX AU", "A$0.16", "-", "-", "-", "-"],
        ["Arrow Exploration", "AXL LN/CN", "£0.50", "-", "-", "-", "-"],
        ["Criterium Energy", "CEQ CN", "C$0.40", "-", "-", "-", "-"],
        ["New Zealand Energy", "NZ CN", "C$1.45", "-", "-", "-", "-"],
        ["Valeura Energy", "VLE CN", "C$16.00", "-", "-", "-", "-"]
    ]
    for row in metrics: ws_metrics.append(row)
    
    # Sheet 2: News & Updates
    ws_news = wb.create_sheet(title="News & Updates")
    ws_news.append(["Category / Region", "Company", "Ticker", "Target Price / Offer", "Key Highlights & Updates"])
    
    news = [
        ("Auctus Publications", "ADX Energy", "ADX AU", "A$0.16", "Solicitó un 3er permiso de exploración en el Canal de Sicilia (370 C.R-AU, 517 km²). Totaliza ~1,650 km² en la zona."),
        ("Auctus Publications", "Arrow Exploration", "AXL LN/CN", "£0.50", "Producción superó los 6,000 boe/d. Construyendo 5 bodegas más en plataforma Icaco (15 en total)."),
        ("Auctus Publications", "Criterium Energy", "CEQ CN", "C$0.40", "Contrato definitivo de venta de gas (GSA) hasta 2040 con PGN (US$6.5-7.6/mcf). Primer gas en 3-4 semanas."),
        ("Auctus Publications", "New Zealand Energy", "NZ CN", "C$1.45", "Producción 2Q26 de 223 boe/d, subiendo a ~570 en 4Q26 y ~700 en 1Q27. En conversaciones para financiamiento de NZ$25M."),
        ("Auctus Publications", "Valeura Energy", "VLE CN", "C$16.00", "Acelera desarrollo de Wassana a 2Q27. Ajusta CapEx 2026 a US$220-235M y aumenta producción 2027 en +1.2 mbbl/d."),
        ("Americas", "Alvopetro Energy", "ALV CN", "n.a.", "Hallazgo de gas en pozo 183-H2 (Brasil) con 44.4m net pay. Ventas de agosto alcanzaron 3,124 boe/d."),
        ("Americas", "Diversified Energy", "DEC US/LN", "n.a.", "Adquiere Birch Permian por US$1.8B (+68 mboe/d de producción y 1.17 bcfe de reservas proven)."),
        ("Americas", "Eni", "ENI IM", "n.a.", "Adquiere junto a YPF un 50% de participación en el bloque OFF-5 en Uruguay."),
        ("Americas", "GeoPark", "GPRK US", "n.a.", "Entrada a Venezuela adquiriendo 65% WI del bloque Bare (Faja del Orinoco). Meta de 75-85 mbbl/d para 2030."),
        ("Americas", "KEO Energy", "KEOC SS", "n.a.", "Acuerdos operativos/financieros con PDVSA para PetroUrdaneta. Cancela fusión con Lionheart."),
        ("Americas", "Shell", "SHEL LN", "n.a.", "Adquiere 50% en bloque Tupinambá (Brasil) y 30% en 5 licencias del prospecto Conifer (Golfo de México)."),
        ("Americas", "Venezuela Majors", "ENI / CVX", "n.a.", "Eni firma contrato a 25 años en Junín-5. Chevron prevé invertir US$7B en 5 años en Petroindependencia."),
        ("Asia Pacific", "Osaka Gas", "-", "n.a.", "Desinvierte su 10% en Greater Sunrise hacia Timor Gas & Petróleo."),
        ("Asia Pacific", "Sunda Energy", "SNDA LN", "n.a.", "Prospecto Halcon (Filipinas) estimado en 8 Tcf 2U (3.0 Tcf netos) con 24% CoS."),
        ("Europe", "EnQuest", "ENQ LN", "n.a.", "Producción 1H26 de 41,544 boe/d. Deuda neta en US$517M. Mantiene guía CapEx en US$720M."),
        ("Europe", "Horizon Petroleum", "HPL LN", "n.a.", "Operaciones de pesca exitosas en pozo L7 (Polonia), confirmando presencia de gas en el Devónico."),
        ("Middle East & Africa", "DNO / Capricorn", "DNO NO / CNE LN", "US$5.214/sh", "Oferta recomendada de DNO para adquirir Capricorn Energy + dividendo especial de US$0.99/sh."),
        ("Middle East & Africa", "BW Energy / Chariot", "BWE NO / CHAR LN", "US$260M base", "Etu Energias adquiere participaciones en Bloques 14K (Angola) de Chevron."),
        ("Middle East & Africa", "Recon Africa", "RECO CN", "C$0.73/sh", "Levantó C$19M en capital para financiar la perforación Kavango West 1X en Namibia."),
        ("Events to Watch", "Energean", "ENOG LN", "1H26 Results", "Presentación de resultados financieros del 1H26 programada para el 09/09/2026.")
    ]
    for row in news: ws_news.append(row)
    
    file_path = "Auctus_Coverage_and_News_2026.xlsx"
    wb.save(file_path)
    print(f"✅ Archivo '{file_path}' guardado correctamente.")

# ==========================================
# 2. SINCRONIZACIÓN CON WORKSPACE
# ==========================================
def sync_to_workspace():
    print("\n=== [2/3] Sincronizando con Google Workspace ===")
    workspace_dir = os.path.expanduser("~/storage/shared/GoogleDrive/Workspace_M82")
    os.makedirs(workspace_dir, exist_ok=True)
    
    src = "Auctus_Coverage_and_News_2026.xlsx"
    dst = os.path.join(workspace_dir, src)
    
    shutil.copy(src, dst)
    print(f"🔄 Sincronizado en: {dst}")

# ==========================================
# 3. PIPELINE DE ALERTAS (TELEGRAM BOT)
# ==========================================
def generate_telegram_alerts():
    print("\n=== [3/3] Generando Payload de Alertas Telegram ===")
    df = pd.read_excel("Auctus_Coverage_and_News_2026.xlsx", sheet_name="News & Updates")
    alerts = df[df['Category / Region'] == 'Auctus Publications']
    
    print("🚨 *[M82-SOVEREIGN ALERT SYSTEM]* 🚨\n")
    for _, row in alerts.iterrows():
        print(f"📌 *{row['Company']}* ({row['Ticker']}) | Target Price: *{row['Target Price / Offer']}*")
        print(f"   └── {row['Key Highlights & Updates']}\n")

if __name__ == "__main__":
    build_master_database()
    sync_to_workspace()
    generate_telegram_alerts()
