import os
import pandas as pd
import yfinance as yf

from langsmith import traceable

import alpaca_trade_api as tradeapi

BASE_URL = 'https://paper-api.alpaca.markets'

# load environment variables
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')


#############################
# Portfolio Agent Functions #
#############################

@traceable(run_type="tool")
def place_order(symbol: str, qty: int, side: str):
    """
    Place a buy or sell market order for a given stock.

    Args:
        symbol (str): The stock ticker (e.g., "AAPL").
        qty (int): Number of shares to trade.
        side (str): Either 'buy' or 'sell'.

    Returns:
        dict: The order response or error message.
    """
    side = side.lower()
    if side not in ['buy', 'sell']:
        return {"error": "Invalid side. Use 'buy' or 'sell'."}

    # Check if the market is open
    clock = api.get_clock()
    if not clock.is_open:
        return {"error": "Market is closed. Cannot place orders."}

    # If selling, check position
    if side == 'sell':
        try:
            position = api.get_position(symbol)
            if int(position.qty) < qty:
                return {"error": f"Not enough shares to sell. You only have {position.qty}."}
        except tradeapi.rest.APIError:
            return {"error": f"No position found for {symbol}."}

    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force='gtc'
        )
        return {"status": "success", "message": f"{side.title()} order submitted for {qty} share(s) of {symbol}", "order": order._raw}
    except Exception as e:
        return {"error": str(e)}

# # Example usage
# response = place_order("TSLA", 10, "buy")
# print(response)

# response = place_order("AAPL", 1, "sell")
# print(response)


@traceable(run_type="tool")
def get_portfolio_state():
    """
    Retrieves and prints the current state of the Alpaca paper trading portfolio.

    Returns:
        dict: Portfolio summary including cash, equity, positions, and more.
    """
    try:
        account = api.get_account()
        positions = api.list_positions()

        portfolio_summary = {
            "cash": account.cash,
            "buying_power": account.buying_power,
            "portfolio_value": account.portfolio_value,
            "equity": account.equity,
            "positions": []
        }

        for p in positions:
            portfolio_summary["positions"].append({
                "symbol": p.symbol,
                "qty": p.qty,
                "avg_entry_price": p.avg_entry_price,
                "current_price": p.current_price,
                "market_value": p.market_value,
                "unrealized_pl": p.unrealized_pl,
                "unrealized_plpc": f"{float(p.unrealized_plpc) * 100:.2f}%"
            })

        return portfolio_summary

    except Exception as e:
        return {"error": str(e)}

# # Example usage
# portfolio = get_portfolio_state()
# for item in portfolio:
#     print(f"{item}: {portfolio[item]}")

