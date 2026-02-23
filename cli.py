import argparse
from bot.orders import OrderService
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    service = OrderService()
    service.create_order(
        symbol=args.symbol.upper(),
        side=args.side.upper(),
        order_type=args.type.upper(),
        quantity=args.quantity,
        price=args.price
    )

if __name__ == "__main__":
    main()