import requests

API_URL = "https://api1.api.cbtraderbd.xyz"

def stream_pocket_candles(pair="EURUSD_otc"):
    print(f"Connecting to PocketOption WebSocket stream for {pair} at {API_URL}...")

if __name__ == "__main__":
    stream_pocket_candles()
