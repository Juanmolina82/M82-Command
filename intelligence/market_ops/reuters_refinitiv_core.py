import datetime
import time

# Data extraída de tus capturas (G20, Emerging Markets, etc.)
REUTERS_MATRIX = {
    "G20_EQUITY": "<G20/EQUITY>",
    "EMG_MARKETS": "<EMG/EQUITY1>",
    "WORLD_INDICES": "<WORLD/INDICES1>",
    "EQUITY_DERIV": "<EQUITY/DERIV>",
    "GLOBAL_FUNDS": "<FUNDS>",
    "ENERGY_SECTOR": "<ENERGY/EQUITY>"
}

def stream_intel():
    print("\033[1;34m[M82-REUTERS CORE: INJECTING REAL-TIME GUIDES]\033[0m")
    with open("M82_MasterLog.txt", "a") as f:
        for name, code in REUTERS_MATRIX.items():
            ts = datetime.datetime.now().strftime("%H:%M:%S")
            line = f"[{ts}] REUTERS_INTEL: {name} | CODE: {code} | STATUS: STREAMING"
            print(line)
            f.write(line + "\n")
            time.sleep(0.3)

if __name__ == "__main__":
    stream_intel()
