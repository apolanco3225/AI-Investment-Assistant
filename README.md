# AI Investment Assistant

A multi-agent system for investment portfolio management and company research using LangGraph and LangChain.

## Overview

This project implements a multi-agent system that combines portfolio management capabilities with company research functionality. The system uses a supervisor agent to coordinate between specialized agents that handle different aspects of investment management.

## Architecture

The system consists of three main components:

1. **Supervisor Agent**: Coordinates and routes user requests to the appropriate specialized agent
2. **Portfolio Manager Agent**: Handles portfolio-related tasks and trading operations
3. **Company Info Agent**: Provides detailed information about companies and stocks

### Workflow Diagram

![Multi-Agent Workflow](workflow_diagram.png)

## Features

### Portfolio Manager Agent
- View current portfolio state
- Execute buy/sell orders
- Track positions and performance
- Monitor cash and buying power

### Company Info Agent
- Retrieve detailed company information
- Access financial metrics
- Get market data
- View company profiles and risk assessments

## Technical Implementation

The system is built using:
- LangGraph for agent orchestration
- LangChain for agent creation and tool management
- Alpaca API for trading operations
- yfinance for company data

## Setup

1. Install required dependencies:
```bash
pip install langchain langgraph alpaca-trade-api yfinance
```

2. Set up environment variables:
```bash
export ALPACA_API_KEY="your_api_key"
export ALPACA_SECRET_KEY="your_secret_key"
```

## Usage

The system can be used through a Jupyter notebook interface. Example queries:

- "What is the current state of my portfolio?"
- "Can you give me information about NVIDIA?"
- "Buy 10 shares of AAPL"
- "Sell 5 shares of MSFT"

## Agents

### Supervisor Agent
The supervisor agent acts as the main coordinator, interpreting user requests and delegating them to the appropriate specialized agent. It ensures smooth communication between agents and maintains context throughout the conversation.

### Portfolio Manager Agent
Handles all portfolio-related operations:
- Portfolio state monitoring
- Order execution
- Position tracking
- Performance analysis

### Company Info Agent
Provides comprehensive company research:
- Company profiles
- Financial metrics
- Market data
- Risk assessments

## Contributing

Feel free to submit issues and enhancement requests!
