import time
import datetime

REUTERS_EQUITY_GUIDES = {
    "G20_COUNTRIES": "<G20/EQUITY>",
    "EMERGING_MARKETS": "<EMG/EQUITY1>",
    "EUROPEAN_EQUITIES": "<EUR/EQUITY>",
    "WORLD_INDICES": "<WORLD/INDICES1>",
    "GLOBAL_FUNDS": "<FUNDS>",
    "EQUITY_DERIVATIVES": "<EQUITY/DERIV>"
}

def stream_reuters_intel():
    print(f"\n[M82 REUTERS INTEL CORE - ACTIVE]")
    for category, code in REUTERS_EQUITY_GUIDES.items():
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_line = f"[{timestamp}] REUTERS_GUIDE: {category} | ACCESS_CODE: {code} | STATUS: READY"
        print(log_line)
        with open("M82_MasterLog.txt", "a") as f:
            f.write(log_line + "\n")
        time.sleep(0.5)

if __name__ == "__main__":
    stream_reuters_intel()
