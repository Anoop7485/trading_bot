import time
import hmac
import hashlib
import requests
import os
import logging
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("BinanceClient")

class BinanceFuturesClient:
    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.secret_key = os.getenv("BINANCE_SECRET_KEY")

        if not self.api_key or not self.secret_key:
            raise ValueError("API keys missing in .env file")

    def _generate_signature(self, query_string):
        return hmac.new(
            self.secret_key.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

    def _request(self, method, endpoint, params=None):
        if params is None:
            params = {}

        params["timestamp"] = int(time.time() * 1000)
        params["recvWindow"] = 5000

        query_string = urlencode(params)
        signature = self._generate_signature(query_string)
        query_string += f"&signature={signature}"

        headers = {"X-MBX-APIKEY": self.api_key}
        url = f"{self.BASE_URL}{endpoint}?{query_string}"

        logger.info(f"REQUEST: {method} {url}")

        try:
            response = requests.request(method, url, headers=headers, timeout=10)
            logger.info(f"RESPONSE: {response.text}")

            if response.status_code != 200:
                raise Exception(response.json())

            return response.json()

        except requests.exceptions.RequestException as e:
            logger.error(f"NETWORK ERROR: {e}")
            raise Exception("Network error occurred")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": str(quantity)
        }

        if order_type == "LIMIT":
            params["price"] = str(price)
            params["timeInForce"] = "GTC"

        return self._request("POST", endpoint, params)