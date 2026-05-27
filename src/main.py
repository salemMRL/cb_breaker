from braw import signed_get
from data import get_klines
from indicators import ema, rsi, sma


def main():

    # 1. Connection test
    account = signed_get("/api/v3/account")

    print("CONNECTED")

    balances = account["balances"]

    for b in balances:
        if float(b["free"]) > 0:
            print(b)

    # 2. Download market data
    df = get_klines(symbol="BTCUSDT", interval="1m", limit=200)

    print(df.head())

    # 3. Generate indicators
    df["sma_20"] = sma(df["close"], 20)

    df["ema_20"] = ema(df["close"], 20)

    df["rsi_14"] = rsi(df["close"], 14)

    print(df.tail(20))

    # 4. Save dataset
    df.to_csv("btc_with_indicators.csv", index=False)

    print("DATA SAVED")


if __name__ == "__main__":
    main()
