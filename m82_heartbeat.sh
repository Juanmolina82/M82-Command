#!/bin/bash
cd /data/data/com.termux/files/home/M82_Fusion/molina-algorithm
# Ejecución con ruta verificada
python3 intelligence/market_ops/wallstreet_fusion.py
# Sincronización a GitHub
git add .
git commit -m "M82 Heartbeat: Wall Street Sync $(date)"
git push origin main
