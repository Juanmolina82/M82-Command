#!/bin/bash
while true; do
  python3 intelligence/market_ops/watchdog_reuters.py
  sleep 300 # Escanea cada 5 minutos
done
