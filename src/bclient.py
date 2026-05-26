import time

from binance.spot import Spot

from config import BINANCE_API_KEY, BINANCE_API_SECRET, BINANCE_BASE_URL

client = Spot(
    api_key=BINANCE_API_KEY,
    api_secret=BINANCE_API_SECRET,
    base_url=BINANCE_BASE_URL,
)

# Get Binance server time
server_time = client.time()["serverTime"]

# Local machine time
local_time = int(time.time() * 1000)

# Calculate offset
TIME_OFFSET = server_time - local_time

print(f"Time offset: {TIME_OFFSET} ms")
