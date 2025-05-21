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
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor

# Local imports
from agent_tools.portfolio_manager_tools import place_order, get_portfolio_state
from agent_tools.financial_analyst_tools import (
    get_analyst_price_targets,
    get_recommendations,
    get_fundamental_analysis,
    get_technical_analysis,
)
from agent_tools.company_research_tools import (
    get_basic_info,
    get_quarterly_report,
    search_financial_news,
    get_balance_sheet,
)

# Load configuration from YAML file
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

# Configure LangSmith environment for tracing and monitoring
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = config["project_name"]

# Create Portfolio Manager Agent
# This agent is responsible for managing investment portfolios, executing trades,
# and monitoring portfolio state
model_portfolio_manager = ChatOpenAI(
    model=config["models"]["portfolio_manager"]["model"],
    temperature=config["models"]["portfolio_manager"]["temperature"],
)

prompt_portfolio_manager = hub.pull(
    config["models"]["portfolio_manager"]["prompt_handler"]
)[0].prompt.template

portfolio_manager_agent = create_react_agent(
    model=model_portfolio_manager,
    tools=[place_order, get_portfolio_state],
    name=config["models"]["portfolio_manager"]["agent_name"],
    prompt=prompt_portfolio_manager,
)

# Create Financial Analyst Agent
# This agent performs detailed financial analysis including:
# - Price target analysis
# - Investment recommendations
# - Fundamental analysis
# - Technical analysis
model_financial_analyst = ChatOpenAI(
    model=config["models"]["financial_analyst"]["model"],
    temperature=config["models"]["financial_analyst"]["temperature"],
)

prompt_financial_analyst = hub.pull(
    config["models"]["financial_analyst"]["prompt_handler"]
)[0].prompt.template

financial_analyst_agent = create_react_agent(
    model=model_financial_analyst,
    tools=[
        get_analyst_price_targets,
        get_recommendations,
        get_fundamental_analysis,
        get_technical_analysis,
    ],
    name=config["models"]["financial_analyst"]["agent_name"],
    prompt=prompt_financial_analyst,
)

# Create Company Research Agent
# This agent gathers comprehensive company information including:
# - Basic company information
# - Quarterly reports
# - Financial news
# - Balance sheet data
model_company_researcher = ChatOpenAI(
    model=config["models"]["company_researcher"]["model"],
    temperature=config["models"]["company_researcher"]["temperature"],
)

prompt_company_researcher = hub.pull(
    config["models"]["company_researcher"]["prompt_handler"]
)[0].prompt.template

research_agent = create_react_agent(
    model=model_company_researcher,
    tools=[
        get_basic_info,
        get_quarterly_report,
        search_financial_news,
        get_balance_sheet,
    ],
    name=config["models"]["company_researcher"]["agent_name"],
    prompt=prompt_company_researcher,
)

# Create Orchestrator Agent
# This agent coordinates between all other agents, managing the workflow
# and ensuring proper communication between different components
model_orchestrator = ChatOpenAI(
    model=config["models"]["orchestrator"]["model"],
    temperature=config["models"]["orchestrator"]["temperature"],
)

prompt_orchestrator = hub.pull(
    config["models"]["orchestrator"]["prompt_handler"]
)[0].prompt.template

# Create and compile the final workflow
workflow = create_supervisor(
    [portfolio_manager_agent, research_agent, financial_analyst_agent],
    model=model_orchestrator,
    prompt=prompt_orchestrator,
)

# Compile the workflow into an executable graph
graph = workflow.compile()
