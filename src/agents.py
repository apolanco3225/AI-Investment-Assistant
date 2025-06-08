"""
Agent definitions for the AI Investment Assistant.

This module defines and configures various AI agents for investment analysis:
- Portfolio Manager Agent: Handles portfolio operations and state
- Financial Analyst Agent: Performs financial analysis and recommendations
- Company Research Agent: Gathers company information and news
- Orchestrator: Coordinates between different agents
"""

# Standard library imports
import os
import yaml

# Third-party imports
from langchain import hub
from langgraph_supervisor import create_supervisor

# Local imports
from .model_factory import create_agent, create_model, get_model_config
from .agent_tools.portfolio_manager_tools import place_order, get_portfolio_state
from .agent_tools.financial_analyst_tools import (
    get_analyst_price_targets,
    get_recommendations,
    get_fundamental_analysis,
    get_technical_analysis,
)
from .agent_tools.company_research_tools import (
    get_basic_info,
    get_quarterly_report,
    search_financial_news,
    get_balance_sheet,
)

# Load configuration from YAML file
config_path = os.path.join(os.path.dirname(__file__), "..", "config.yml")
with open(config_path, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# Configure LangSmith environment for tracing and monitoring
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = config["project_name"]

# Set the provider to use (can be "openai", "nvidia", or "ollama")
PROVIDER = config["provider"]

# Create Portfolio Manager Agent
# This agent is responsible for managing investment portfolios, executing trades,
# and monitoring portfolio state
portfolio_manager_agent = create_agent(
    PROVIDER,
    "portfolio_manager",
    [place_order, get_portfolio_state]
)

# Create Financial Analyst Agent
# This agent performs detailed financial analysis including:
# - Price target analysis
# - Investment recommendations
# - Fundamental analysis
# - Technical analysis
financial_analyst_agent = create_agent(
    PROVIDER,
    "financial_analyst",
    [
        get_analyst_price_targets,
        get_recommendations,
        get_fundamental_analysis,
        get_technical_analysis,
    ]
)

# Create Company Research Agent
# This agent gathers comprehensive company information including:
# - Basic company information
# - Quarterly reports
# - Financial news
# - Balance sheet data
research_agent = create_agent(
    PROVIDER,
    "company_researcher",
    [
        get_basic_info,
        get_quarterly_report,
        search_financial_news,
        get_balance_sheet,
    ]
)

# Create Orchestrator Agent
# This agent coordinates between all other agents, managing the workflow
# and ensuring proper communication between different components
orchestrator_model = create_model(PROVIDER, "orchestrator")
orchestrator_prompt = hub.pull(get_model_config(PROVIDER, "orchestrator")["prompt_handler"])[0].prompt.template

# Create and compile the final workflow
workflow = create_supervisor(
    [portfolio_manager_agent, research_agent, financial_analyst_agent],
    model=orchestrator_model,
    prompt=orchestrator_prompt,
)

# Compile the workflow into an executable graph
graph = workflow.compile()
