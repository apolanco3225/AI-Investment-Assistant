import pytest
from agent_tools.financial_analyst_tools import (
    get_fundamental_analysis,
    get_technical_analysis,
    get_analyst_price_targets,
    get_recommendations
)
from unittest.mock import patch
import pandas as pd

def test_get_fundamental_analysis(mock_yfinance):
    with patch('yfinance.Ticker', return_value=mock_yfinance):
        analysis = get_fundamental_analysis("AAPL")
        assert "valuation" in analysis
        assert "profitability" in analysis
        assert "growth" in analysis
        assert "financial_strength" in analysis
        assert "cash_flow" in analysis

def test_get_technical_analysis():
    with patch('yfinance.download') as mock_download:
        # Mock historical data
        mock_data = pd.DataFrame({
            'Close': [100, 101, 102, 103, 104],
            'Open': [99, 100, 101, 102, 103],
            'High': [101, 102, 103, 104, 105],
            'Low': [98, 99, 100, 101, 102],
            'Volume': [1000, 1100, 1200, 1300, 1400]
        })
        mock_download.return_value = mock_data

        result = get_technical_analysis(
            "AAPL",
            start_date="2024-01-01",
            end_date="2024-01-31",
            indicators=["SMA", "RSI"]
        )
        
        assert "historical_prices" in result
        assert "indicators" in result
        assert "SMA_20" in result["indicators"]
        assert "RSI_14" in result["indicators"]

def test_get_analyst_price_targets(mock_yfinance):
    with patch('yfinance.Ticker', return_value=mock_yfinance):
        targets = get_analyst_price_targets("AAPL")
        assert isinstance(targets, pd.DataFrame)

def test_get_recommendations(mock_yfinance):
    with patch('yfinance.Ticker', return_value=mock_yfinance):
        recommendations = get_recommendations("AAPL")
        assert isinstance(recommendations, pd.DataFrame) 