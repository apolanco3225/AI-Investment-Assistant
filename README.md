[![Python application test with Github Actions](https://github.com/apolanco3225/AI-Investment-Assistant/actions/workflows/main.yml/badge.svg)](https://github.com/apolanco3225/AI-Investment-Assistant/actions/workflows/main.yml)

# AI Investment Assistant

A multi-agent system for investment portfolio management and company research using LangGraph and LangChain.

![Image](https://github.com/user-attachments/assets/33b5e053-3c7b-4601-81de-5814fb664c43)

## Overview

This project implements a multi-agent system that combines portfolio management capabilities with company research and financial analysis functionality. The system uses a supervisor agent to coordinate between specialized agents that handle different aspects of investment management.

## Quick Start

The easiest way to run the application is using the dev server:

1. Start the dev server:
```bash
make dev-server
```

2. Once the server is ready, you'll see:
```
Ready!

- API: http://localhost:2024
- Docs: http://localhost:2024/docs
- LangGraph Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
```

3. You can interact with the application through:
   - API: Access the REST API at `http://localhost:2024`
   - API Documentation: View the OpenAPI documentation at `http://localhost:2024/docs`
   - LangGraph Studio: Monitor and debug your agent workflows at `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`

## Architecture

The system consists of four main components:

1. **Supervisor Agent**: Coordinates and routes user requests to the appropriate specialized agent
2. **Portfolio Manager Agent**: Handles portfolio-related tasks and trading operations
3. **Financial Analyst Agent**: Provides technical and fundamental analysis of stocks
4. **Company Research Agent**: Provides detailed information about companies and stocks

### Workflow Diagram

![Image](https://github.com/user-attachments/assets/dd9e9246-685a-427e-924c-8d3cb7c52a87)

## Features

### Portfolio Manager Agent
- View current portfolio state
- Execute buy/sell orders
- Track positions and performance
- Monitor cash and buying power

### Financial Analyst Agent
- Get analyst price targets
- Receive investment recommendations
- Access fundamental analysis
- View technical analysis indicators

### Company Research Agent
- Retrieve detailed company information
- Access quarterly financial reports
- Search financial news
- View balance sheet data

## Project Structure

```
.
├── src/                # Source code directory
│   ├── agent_tools/    # Custom tools for each agent
│   ├── mcp_servers/    # Multi-agent communication protocol servers
│   ├── agents.py       # Agent definitions and configurations
│   └── main.py        # Main script for command line execution
├── .langgraph_api/     # LangGraph API configuration
├── config.yml          # Configuration settings
├── langgraph.json      # LangGraph workflow configuration
├── multi_agent_workflow.ipynb  # Jupyter notebook for workflow development
├── Makefile           # Build and deployment automation
└── pyproject.toml     # Python project configuration
```

## Technical Implementation

The system is built using:
- LangGraph for agent orchestration
- LangChain for agent creation and tool management
- OpenAI GPT-4 for natural language processing
- Alpaca API for trading operations
- yfinance for market data
- Tavily for news search

## Testing

The project includes comprehensive test coverage using pytest. Tests are automatically run through GitHub Actions on every push and pull request.

### Running Tests Locally

1. Install test dependencies:
```bash
uv pip install -r requirements-test.txt
```

2. Run the test suite:
```bash
pytest
```

3. Run tests with coverage report:
```bash
pytest --cov=.
```

### Test Structure

```
.
├── tests/
│   ├── unit/           # Unit tests for individual components
│   ├── integration/    # Integration tests for agent interactions
│   └── e2e/           # End-to-end tests for complete workflows
```

### Continuous Integration

The project uses GitHub Actions for continuous integration. The workflow:
- Runs on every push and pull request
- Executes the full test suite
- Generates coverage reports
- Validates code style and formatting

## Setup

1. Install the project and its dependencies:
```bash
uv pip install .
```

2. Set up environment variables:
```bash
export OPENAI_API_KEY="your_openai_api_key"
export ALPACA_API_KEY="your_alpaca_api_key"
export ALPACA_SECRET_KEY="your_alpaca_secret_key"
export TAVILY_API_KEY="your_tavily_api_key"
```

## Usage

### Command Line Execution

To run the system through the command line interface:

```bash
uv run src/main.py "What is the current state of my portfolio?"
```

Example queries:
- "What is the current state of my portfolio?"
- "Can you give me information about NVIDIA?"
- "Buy 10 shares of AAPL"
- "Sell 5 shares of MSFT"
- "What are the analyst price targets for GOOGL?"
- "Show me the technical analysis for MSFT"

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
