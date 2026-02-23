
# trading_bot
## Binance Futures Order Execution Bot
### Project Overview

This is a simple Python trading bot that places MARKET and LIMIT orders on Binance Futures Testnet and logs order details clearly.

The project demonstrates:

REST API integration

Secure authentication

Order execution logic

Structured logging

It uses the testnet of
Binance for safe trading practice.

### Features

* Execute MARKET orders

* Execute LIMIT orders

* Secure API keys using .env

* Timestamped order logging

* Clean and modular Python code

### Setup Instructions
1️. Clone the Repository
git clone <your-repo-link>
cd binance-futures-bot
2️. Install Dependencies
pip install -r requirements.txt
3️. Configure Environment Variables

*** Create a .env file and add: ***

API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key
BASE_URL=https://testnet.binancefuture.com
### How to Run
#### MARKET Order
python src/main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
#### LIMIT Order
python src/main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000
### Logging

All orders are recorded in:

logs/bot.log

Each log entry includes:

Timestamp

Order Type (MARKET / LIMIT)

Symbol

Quantity

Price (for LIMIT orders)

API response

The log file contains:

At least one MARKET order

At least one LIMIT order

### Requirements

Python 3.9+

requests

python-dotenv

### Assumptions

Using Binance Futures Testnet

Testnet account has sufficient balance

BTCUSDT used for demonstration

LIMIT orders may remain in NEW status if price is not reached




