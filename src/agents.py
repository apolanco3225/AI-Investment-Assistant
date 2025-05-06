"""
Agent definitions for the AI Investment Assistant.
"""

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor

from .config import MODEL_CONFIG, AGENT_PROMPTS
from .tools import (
    # Portfolio manager tools
    place_order,
    get_portfolio_state,
    
    # Financial analyst tools
    get_analyst_price_targets,
    get_recommendations,
    get_fundamental_analysis,
    get_technical_analysis,
    
    # Company research tools
    get_basic_info,
    get_quarterly_report,
    search_financial_news,
    get_balance_sheet
)

def create_llm():
    """Create and return the language model instance."""
    return ChatOpenAI(
        model=MODEL_CONFIG["model_name"],
        temperature=MODEL_CONFIG["temperature"]
    )

def create_portfolio_manager_agent(model):
    """Create and return the portfolio manager agent."""
    return create_react_agent(
        model=model,
        tools=[place_order, get_portfolio_state],
        name="portfolio_manager",
        prompt=AGENT_PROMPTS["portfolio_manager"]
    )

def create_financial_analyst_agent(model):
    """Create and return the financial analyst agent."""
    return create_react_agent(
        model=model,
        tools=[
            get_analyst_price_targets,
            get_recommendations,
            get_fundamental_analysis,
            get_technical_analysis
        ],
        name="financial_analyst",
        prompt=AGENT_PROMPTS["financial_analyst"]
    )

def create_research_agent(model):
    """Create and return the company research agent."""
    return create_react_agent(
        model=model,
        tools=[
            get_basic_info,
            get_quarterly_report,
            search_financial_news,
            get_balance_sheet
        ],
        name="company_research",
        prompt=AGENT_PROMPTS["company_research"]
    )

def create_workflow():
    """Create and return the complete agent workflow."""
    model = create_llm()
    
    # Create individual agents
    portfolio_manager = create_portfolio_manager_agent(model)
    financial_analyst = create_financial_analyst_agent(model)
    research_agent = create_research_agent(model)
    
    # Create supervisor workflow
    workflow = create_supervisor(
        [portfolio_manager, research_agent, financial_analyst],
        model=model,
        prompt=AGENT_PROMPTS["supervisor"]
    )
    
    return workflow.compile() 