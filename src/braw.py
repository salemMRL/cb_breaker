import hashlib
import hmac
import os
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY").strip()
API_SECRET = os.getenv("BINANCE_API_SECRET").strip().encode()
BASE_URL = os.getenv("BINANCE_BASE_URL", "https://testnet.binance.vision").strip()


def get_server_time():
    r = requests.get(f"{BASE_URL}/api/v3/time", timeout=10)
    r.raise_for_status()
    return r.json()["serverTime"]


def signed_get(path, params=None):
    params = params or {}
    params["timestamp"] = get_server_time()
    params["recvWindow"] = 60000

    query = urlencode(params)
    signature = hmac.new(API_SECRET, query.encode(), hashlib.sha256).hexdigest()

    headers = {"X-MBX-APIKEY": API_KEY}

    url = f"{BASE_URL}{path}?{query}&signature={signature}"

    r = requests.get(url, headers=headers, timeout=10)
    print("STATUS:", r.status_code)
    print("RESPONSE:", r.text)
    r.raise_for_status()
    return r.json()
