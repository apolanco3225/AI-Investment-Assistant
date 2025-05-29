"""
Test data for the AI Investment Assistant.

This module contains reference trajectories and test data used for testing
the various agents and their interactions.
"""

# Reference trajectory for company researcher agent
reference_trajectory_company_researcher = [
    {
        'role': 'assistant',
        'name': 'supervisor',
        'tool_calls': [
            {
                'type': 'function',
                'function': {
                    'name': 'transfer_to_company_researcher',
                    'arguments': '{}'
                }
            }
        ]
    },
    {
        'role': 'tool',
        'name': 'transfer_to_company_researcher'
    },
    {
        'role': 'assistant',
        'name': 'company_researcher'
    },
    {
        'role': 'assistant',
        'name': 'company_researcher',
        'tool_calls': [
            {
                'type': 'function',
                'function': {
                    'name': 'transfer_back_to_supervisor',
                    'arguments': '{}'
                }
            }
        ]
    },
    {
        'role': 'tool',
        'name': 'transfer_back_to_supervisor'
    },
    {
        'role': 'assistant',
        'name': 'supervisor'
    }
]

# Reference trajectory for portfolio manager agent
reference_trajectory_portfolio_manager = [
    {
        'role': 'assistant',
        'name': 'supervisor',
        'tool_calls': [
            {
                'type': 'function',
                'function': {
                    'name': 'transfer_to_portfolio_manager', 
                    'arguments': '{}'
                }
            }
        ]
    },
    {
        'role': 'tool',
        'name': 'transfer_to_portfolio_manager'
    },
    {
        'role': 'assistant',
        'name': 'portfolio_manager'
    },
    {
        'role': 'assistant',
        'name': 'portfolio_manager',
        'tool_calls': [
            {
                'type': 'function',
                'function': {
                    'name': 'transfer_back_to_supervisor', 
                    'arguments': '{}'
                }
            }
        ]
    },
    {
        'role': 'tool',
        'name': 'transfer_back_to_supervisor'
    },
    {
        'role': 'assistant',
        'name': 'supervisor'
    }
]

# Reference trajectory for financial analyst agent
reference_trajectory_financial_analyst = [
    {
        'role': 'assistant',
        'name': 'supervisor',
        'tool_calls': [
            {
                'type': 'function',
                'function': {
                    'name': 'transfer_to_financial_analyst',
                    'arguments': '{}'
                }
            }
        ]
    },
    {
        'role': 'tool',
        'name': 'transfer_to_financial_analyst'
    },
    {
        'role': 'assistant',
        'name': 'financial_analyst'
    },
    {
        'role': 'assistant',
        'name': 'financial_analyst',
        'tool_calls': [
            {
                'type': 'function',
                'function': {
                    'name': 'transfer_back_to_supervisor',
                    'arguments': '{}'
                }
            }
        ]
    },
    {
        'role': 'tool',
        'name': 'transfer_back_to_supervisor'
    },
    {
        'role': 'assistant',
        'name': 'supervisor'
    }
]