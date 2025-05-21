import yfinance as yf
import pandas as pd

def get_analyst_price_targets(ticker):
    """
    Get analyst price targets for a stock using yfinance.
    Args:
        ticker (str): The stock ticker symbol.
    Returns:
        dict: A dictionary containing analyst price targets for the stock.
    """
    stock = yf.Ticker(ticker)
    price_targets = stock.analyst_price_targets
    return price_targets

def get_recommendations(ticker):
    """
    Get analyst recommendations for a stock using yfinance.
    Args:
        ticker (str): The stock ticker symbol.
    Returns:
        DataFrame: A DataFrame containing analyst recommendations for the stock.
    """
    stock = yf.Ticker(ticker)
    recommendations = stock.recommendations
    return recommendations




def get_fundamental_analysis(ticker_symbol: str) -> dict:
    """
    Retrieves a broad set of fundamental analysis data for a given stock ticker using Yahoo Finance.

    Parameters:
    -----------
    ticker_symbol : str
        The stock ticker symbol (e.g., 'AAPL', 'MSFT').

    Returns:
    --------
    dict
        A dictionary grouped by category with the following metrics:

        **Valuation:**
        - 'trailingPE': Price to Earnings (TTM)
        - 'forwardPE': Forward Price to Earnings
        - 'priceToBook': Price to Book Ratio
        - 'enterpriseToRevenue': Enterprise Value / Revenue
        - 'enterpriseToEbitda': Enterprise Value / EBITDA

        **Profitability:**
        - 'returnOnEquity': Return on Equity
        - 'returnOnAssets': Return on Assets
        - 'grossMargins': Gross Margin
        - 'operatingMargins': Operating Margin
        - 'profitMargins': Net Profit Margin

        **Growth:**
        - 'earningsQuarterlyGrowth': EPS Growth YoY
        - 'revenueGrowth': Revenue Growth YoY

        **Financial Strength:**
        - 'totalDebt': Total Debt
        - 'debtToEquity': Debt to Equity Ratio
        - 'currentRatio': Current Ratio
        - 'quickRatio': Quick Ratio
        - 'totalCash': Total Cash
        - 'totalAssets': Total Assets

        **Cash Flow:**
        - 'operatingCashflow': Cash from Operations
        - 'freeCashflow': Free Cash Flow
    """
    stock = yf.Ticker(ticker_symbol)
    info = stock.info

    return {
        "valuation": {
            "trailingPE": info.get("trailingPE"),
            "forwardPE": info.get("forwardPE"),
            "priceToBook": info.get("priceToBook"),
            "enterpriseToRevenue": info.get("enterpriseToRevenue"),
            "enterpriseToEbitda": info.get("enterpriseToEbitda"),
        },
        "profitability": {
            "returnOnEquity": info.get("returnOnEquity"),
            "returnOnAssets": info.get("returnOnAssets"),
            "grossMargins": info.get("grossMargins"),
            "operatingMargins": info.get("operatingMargins"),
            "profitMargins": info.get("profitMargins"),
        },
        "growth": {
            "earningsQuarterlyGrowth": info.get("earningsQuarterlyGrowth"),
            "revenueGrowth": info.get("revenueGrowth"),
        },
        "financial_strength": {
            "totalDebt": info.get("totalDebt"),
            "debtToEquity": info.get("debtToEquity"),
            "currentRatio": info.get("currentRatio"),
            "quickRatio": info.get("quickRatio"),
            "totalCash": info.get("totalCash"),
            "totalAssets": info.get("totalAssets"),
        },
        "cash_flow": {
            "operatingCashflow": info.get("operatingCashflow"),
            "freeCashflow": info.get("freeCashflow"),
        }
    }



def get_technical_analysis(ticker_symbol: str, start_date: str, end_date: str, interval: str = "1d", indicators: list = None) -> dict:
    """
    Retrieves historical price data and computes common technical indicators.

    Parameters:
    -----------
    ticker_symbol : str
        Stock symbol (e.g., 'AAPL', 'MSFT').

    start_date : str
        Start of the time range (e.g., '2023-01-01').

    end_date : str
        End of the time range (e.g., '2024-01-01').

    interval : str
        Data interval ('1d', '1wk', '1mo', etc.). Default is '1d'.

    indicators : list[str]
        List of technical indicators to compute. Options: ['SMA', 'EMA', 'RSI', 'MACD'].

    Returns:
    --------
    dict
        Dictionary with:
        - 'historical_prices': raw OHLCV price data
        - 'indicators': DataFrame containing requested technical indicators
    """
    if indicators is None:
        indicators = ["SMA", "EMA", "RSI", "MACD"]

    data = yf.download(ticker_symbol, start=start_date, end=end_date, interval=interval)
    
    result = {"historical_prices": data.copy()}
    ta = pd.DataFrame(index=data.index)

    close = data["Close"]

    if "SMA" in indicators:
        ta["SMA_20"] = close.rolling(window=20).mean()

    if "EMA" in indicators:
        ta["EMA_20"] = close.ewm(span=20, adjust=False).mean()

    if "RSI" in indicators:
        delta = close.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss
        ta["RSI_14"] = 100 - (100 / (1 + rs))

    if "MACD" in indicators:
        ema12 = close.ewm(span=12, adjust=False).mean()
        ema26 = close.ewm(span=26, adjust=False).mean()
        macd = ema12 - ema26
        signal = macd.ewm(span=9, adjust=False).mean()
        ta["MACD"] = macd
        ta["MACD_Signal"] = signal
        ta["MACD_Hist"] = macd - signal

    result["indicators"] = ta
    return result


