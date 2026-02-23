import logging
from .client import BinanceFuturesClient
from .validators import *

logger = logging.getLogger("OrderService")

class OrderService:

    def __init__(self):
        self.client = BinanceFuturesClient()

    def create_order(self, symbol, side, order_type, quantity, price=None):
        try:
            validate_symbol(symbol)
            validate_side(side)
            validate_order_type(order_type)
            validate_quantity(quantity)
            validate_price(price, order_type)

            print("\n===== ORDER REQUEST SUMMARY =====")
            print(f"Symbol: {symbol}")
            print(f"Side: {side}")
            print(f"Type: {order_type}")
            print(f"Quantity: {quantity}")
            if price:
                print(f"Price: {price}")

            response = self.client.place_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )

            print("\n===== ORDER RESPONSE =====")
            print(f"Order ID: {response.get('orderId')}")
            print(f"Status: {response.get('status')}")
            print(f"Executed Qty: {response.get('executedQty')}")
            print(f"Avg Price: {response.get('avgPrice')}")
            print("\n Order placed successfully")

            return response

        except Exception as e:
            logger.error(f"ORDER FAILED: {e}")
            print(f"\n Order failed: {e}")