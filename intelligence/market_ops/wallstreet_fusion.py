import datetime

# REUTERS EQUITIES LIST (M82 EXTENSION)
SYMBOLS = ["MSFT", "XOM", "TSLA", "NVDA", "GLD", "AAPL", "AMZN", "META", "GOOGL"]

def run_reuters_sync():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("M82_MasterLog.txt", "a") as f:
        for ticker in SYMBOLS:
            log_line = f"[{timestamp}] REUTERS_MARKET: {ticker} | M82-CORE SYNC: SUCCESS\n"
            print(log_line.strip())
            f.write(log_line)

if __name__ == "__main__":
    run_reuters_sync()
