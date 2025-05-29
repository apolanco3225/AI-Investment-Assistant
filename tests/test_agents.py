import pytest
from agentevals.trajectory.llm import create_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE
from langchain_core.messages import HumanMessage
from langchain_core.messages.utils import convert_to_openai_messages
from tests.test_data import (
    reference_trajectory_portfolio_manager,
    reference_trajectory_company_researcher,
    reference_trajectory_financial_analyst
)
from agents import graph

@pytest.fixture
def evaluator():
    return create_trajectory_llm_as_judge(
        prompt=TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE,
        model="openai:o3-mini"
    )

def test_portfolio_manager_trajectory(evaluator):
    # Create human message
    human_msg = HumanMessage(
        content="What is the current state of my portfolio?"
    )

    # Invoke graph
    result = graph.invoke({"messages": human_msg})
    
    # Convert outputs to OpenAI messages format
    outputs = convert_to_openai_messages(result["messages"])
    
    # Get LLM judgement
    llm_judgement = evaluator(
        outputs=outputs,
        reference_outputs=reference_trajectory_portfolio_manager,
    )
    
    # Assert that the score is True
    assert llm_judgement.get('score') is True, "Trajectory score should be True"

def test_company_researcher_trajectory(evaluator):
    # Create human message
    human_msg = HumanMessage(
        content="Can you research Apple Inc. for me?"
    )

    # Invoke graph
    result = graph.invoke({"messages": human_msg})
    
    # Convert outputs to OpenAI messages format
    outputs = convert_to_openai_messages(result["messages"])
    
    # Get LLM judgement
    llm_judgement = evaluator(
        outputs=outputs,
        reference_outputs=reference_trajectory_company_researcher,
    )
    
    # Assert that the score is True
    assert llm_judgement.get('score') is True, "Trajectory score should be True"

def test_financial_analyst_trajectory(evaluator):
    # Create human message
    human_msg = HumanMessage(
        content="What's your analysis of Tesla's financial performance?"
    )

    # Invoke graph
    result = graph.invoke({"messages": human_msg})
    
    # Convert outputs to OpenAI messages format
    outputs = convert_to_openai_messages(result["messages"])
    
    # Get LLM judgement
    llm_judgement = evaluator(
        outputs=outputs,
        reference_outputs=reference_trajectory_financial_analyst,
    )
    
    # Assert that the score is True
    assert llm_judgement.get('score') is True, "Trajectory score should be True"


