"""
Main script to run the AI Investment Assistant workflow.
"""

import argparse
from typing import Dict, Any

from .agents import create_workflow

def process_query(query: str) -> Dict[str, Any]:
    """
    Process a user query through the agent workflow.
    
    Args:
        query: The user's query string
    
    Returns:
        Dict containing the workflow response
    """
    # Create and compile the workflow
    graph = create_workflow()
    
    # Process the query
    result = graph.invoke({
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    })
    
    return result

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="AI Investment Assistant")
    parser.add_argument("query", help="The query to process")
    args = parser.parse_args()
    
    # Process the query
    result = process_query(args.query)
    
    # Print the results
    for message in result["messages"]:
        print(f"\n{'='*32} {message.name} Message {'='*32}\n")
        print(message.content)

if __name__ == "__main__":
    main() 