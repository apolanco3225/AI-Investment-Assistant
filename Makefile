format:
	uv run black *.py

lint:
	uv run pylint --disable=R,C,E0401,E0611 *.py

test:
	uv run pytest tests/ -v

test-agents:
	uv run pytest tests/test_agents.py -v

test-coverage:
	uv run pytest tests/ --cov=agent_tools -v

test-watch:
	uv run pytest tests/ -v -f

all: lint format test 