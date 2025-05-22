import pytest
from agent_tools.company_research_tools import (
    search_financial_news,
    get_basic_info,
    get_balance_sheet,
    get_quarterly_report
)
from unittest.mock import patch, Mock
import pandas as pd

def test_search_financial_news(mock_tavily_client):
    with patch('tavily.TavilyClient', return_value=mock_tavily_client):
        news = search_financial_news("Apple Inc.")
        assert isinstance(news, str)
        assert "Test News 1" in news
        assert "Test News 2" in news

def test_get_basic_info(mock_yfinance):
    with patch('yfinance.Ticker', return_value=mock_yfinance):
        info = get_basic_info("AAPL")
        assert info["longName"] == "Apple Inc."
        assert info["symbol"] == "AAPL"
        assert info["industry"] == "Consumer Electronics"
        assert info["sector"] == "Technology"

def test_get_balance_sheet(mock_yfinance):
    with patch('yfinance.Ticker', return_value=mock_yfinance):
        date, balance_sheet = get_balance_sheet("AAPL")
        assert isinstance(date, str)
        assert isinstance(balance_sheet, pd.Series)

def test_get_quarterly_report():
    with patch('edgar.Company') as mock_company:
        mock_filing = Mock()
        mock_filing.latest.return_value = Mock(obj=lambda: Mock(items=["item1", "item2"]))
        mock_company.return_value.get_filings.return_value = mock_filing
        
        report = get_quarterly_report("AAPL")
        assert isinstance(report, str) 