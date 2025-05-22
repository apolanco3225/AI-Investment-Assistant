import pytest
from agent_tools.portfolio_manager_tools import place_order, get_portfolio_state
from unittest.mock import patch

def test_place_order_buy(mock_alpaca_api):
    with patch('agent_tools.portfolio_manager_tools.api', mock_alpaca_api):
        result = place_order("AAPL", 10, "buy")
        assert result["status"] == "success"
        assert "Buy order submitted" in result["message"]
        mock_alpaca_api.submit_order.assert_called_once()

def test_place_order_sell(mock_alpaca_api):
    with patch('agent_tools.portfolio_manager_tools.api', mock_alpaca_api):
        result = place_order("AAPL", 5, "sell")
        assert result["status"] == "success"
        assert "Sell order submitted" in result["message"]
        mock_alpaca_api.submit_order.assert_called_once()

def test_place_order_invalid_side(mock_alpaca_api):
    with patch('agent_tools.portfolio_manager_tools.api', mock_alpaca_api):
        result = place_order("AAPL", 10, "invalid")
        assert "error" in result
        assert "Invalid side" in result["error"]

def test_get_portfolio_state(mock_alpaca_api):
    with patch('agent_tools.portfolio_manager_tools.api', mock_alpaca_api):
        portfolio = get_portfolio_state()
        assert "cash" in portfolio
        assert "positions" in portfolio
        assert len(portfolio["positions"]) == 1
        assert portfolio["positions"][0]["symbol"] == "AAPL" 