"""
Workflow definitions for connecting agents in the AI Investment Assistant.
"""

from langgraph_supervisor import create_supervisor

from agents import (
    create_llm,
    create_portfolio_manager_agent,
    create_financial_analyst_agent,
    create_research_agent
)
from config import AGENT_PROMPTS

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


graph = create_workflow()