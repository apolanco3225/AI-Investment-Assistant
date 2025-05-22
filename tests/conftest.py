import pytest
import os
from unittest.mock import Mock
import pandas as pd
import yfinance as yf

@pytest.fixture
def mock_alpaca_api():
    mock = Mock()
    # Mock account response
    mock.get_account.return_value = Mock(
        cash="100000.00",
        buying_power="100000.00",
        portfolio_value="150000.00",
        equity="150000.00"
    )
    # Mock positions response
    mock.list_positions.return_value = [
        Mock(
            symbol="AAPL",
            qty="10",
            avg_entry_price="150.00",
            current_price="160.00",
            market_value="1600.00",
            unrealized_pl="100.00",
            unrealized_plpc="0.0625"
        )
    ]
    # Mock clock response
    mock.get_clock.return_value = Mock(is_open=True)
    return mock

@pytest.fixture
def mock_yfinance():
    mock = Mock()
    # Mock stock info
    mock.info = {
        'longName': 'Apple Inc.',
        'symbol': 'AAPL',
        'companyOfficers': [{'name': 'Tim Cook', 'title': 'CEO'}],
        'market': 'us_market',
        'address1': '1 Apple Park Way',
        'city': 'Cupertino',
        'state': 'CA',
        'zip': '95014',
        'country': 'United States',
        'phone': '408-996-1010',
        'website': 'https://www.apple.com',
        'industry': 'Consumer Electronics',
        'sector': 'Technology',
        'longBusinessSummary': 'Apple Inc. designs, manufactures, and markets smartphones...',
        'fullTimeEmployees': 154000
    }
    return mock

@pytest.fixture
def mock_tavily_client():
    mock = Mock()
    mock.search.return_value = {
        'results': [
            {
                'title': 'Test News 1',
                'content': 'This is a test news article about the company...'
            },
            {
                'title': 'Test News 2',
                'content': 'Another test news article...'
            }
        ]
    }
    return mock

@pytest.fixture(autouse=True)
def setup_env_vars():
    # Set up test environment variables
    os.environ["ALPACA_API_KEY"] = "test_key"
    os.environ["ALPACA_SECRET_KEY"] = "test_secret"
    os.environ["TAVILY_API_KEY"] = "test_tavily_key"
    yield
    # Clean up after tests
    os.environ.pop("ALPACA_API_KEY", None)
    os.environ.pop("ALPACA_SECRET_KEY", None)
    os.environ.pop("TAVILY_API_KEY", None) 