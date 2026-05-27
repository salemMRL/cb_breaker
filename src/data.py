import pandas as pd
import requests

BASE_URL = "https://testnet.binance.vision"


def get_klines(symbol="BTCUSDT", interval="1m", limit=500):

    url = f"{BASE_URL}/api/v3/klines"

    params = {"symbol": symbol, "interval": interval, "limit": limit}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(
        data,
        columns=[
            "open_time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "quote_asset_volume",
            "number_of_trades",
            "taker_buy_base",
            "taker_buy_quote",
            "ignore",
        ],
    )

    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")

    numeric_cols = ["open", "high", "low", "close", "volume"]

    df[numeric_cols] = df[numeric_cols].astype(float)

    return df[["open_time", "open", "high", "low", "close", "volume"]]
