"""
Model factory module for creating and configuring different LLM models.

This module provides functions to create and configure different types of language models
from various providers (OpenAI, NVIDIA, Ollama) and create agents with these models.
"""

from typing import Literal, Dict, Any, List
import yaml

from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langgraph.prebuilt import create_react_agent

# Load configuration from YAML file
with open("config.yml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

def get_model_config(provider: Literal["openai", "nvidia", "ollama"], agent_type: str) -> Dict[str, Any]:
    """
    Get the model configuration for a specific provider and agent type.
    
    Args:
        provider: The model provider ("openai", "nvidia", or "ollama")
        agent_type: The type of agent (e.g., "orchestrator", "portfolio_manager")
    
    Returns:
        Dict containing the model configuration
    
    Raises:
        ValueError: If the provider is not found in the configuration
    """
    provider_key = f"{provider}_models"
    if provider_key not in config:
        raise ValueError(f"Provider {provider} not found in configuration")
    return config[provider_key][agent_type]

def create_model(provider: Literal["openai", "nvidia", "ollama"], agent_type: str):
    """
    Create a model instance based on the provider and agent type.
    
    Args:
        provider: The model provider ("openai", "nvidia", or "ollama")
        agent_type: The type of agent (e.g., "orchestrator", "portfolio_manager")
    
    Returns:
        A configured model instance
    
    Raises:
        ValueError: If the provider is not supported
    """
    model_config = get_model_config(provider, agent_type)
    
    if provider == "openai":
        return ChatOpenAI(
            model=model_config["model"],
            temperature=model_config["temperature"],
        )
    elif provider == "nvidia":
        return ChatNVIDIA(
            model=model_config["model"],
            temperature=model_config["temperature"],
        )
    elif provider == "ollama":
        return ChatOllama(
            model=model_config["model"],
            temperature=model_config["temperature"],
        )
    else:
        raise ValueError(f"Unsupported provider: {provider}")

def create_agent(provider: Literal["openai", "nvidia", "ollama"], agent_type: str, tools: List):
    """
    Create an agent with the specified provider, type, and tools.
    
    Args:
        provider: The model provider ("openai", "nvidia", or "ollama")
        agent_type: The type of agent (e.g., "orchestrator", "portfolio_manager")
        tools: List of tools to be used by the agent
    
    Returns:
        A configured agent instance
    """
    model_config = get_model_config(provider, agent_type)
    model = create_model(provider, agent_type)
    
    prompt = hub.pull(model_config["prompt_handler"])[0].prompt.template
    
    return create_react_agent(
        model=model,
        tools=tools,
        name=model_config["agent_name"],
        prompt=prompt,
    ) 