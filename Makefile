format:
	uv run black src/*.py

lint:
	uv run pylint --disable=R,C,E0401,E0611 src/*.py

test:
	uv run pytest tests/ -v

test-agents:
	uv run pytest tests/test_agents.py -v

test-coverage:
	uv run pytest tests/ --cov=agent_tools -v

test-watch:
	uv run pytest tests/ -v -f

install:
	uv venv
	uv pip install -e .

dev-server:
	uv venv .venv --python 3.11
	. .venv/bin/activate && \
	uv pip install -e . && \
	langgraph dev

all: lint format test 

help:
	@echo "Available commands:"
	@echo "  make format        - Format Python code using black"
	@echo "  make lint         - Run pylint checks on Python files"
	@echo "  make test         - Run all tests with verbose output"
	@echo "  make test-agents  - Run specific agent tests"
	@echo "  make test-coverage - Run tests with coverage reporting"
	@echo "  make test-watch   - Run tests in watch mode"
	@echo "  make install      - Set up virtual environment and install package"
	@echo "  make dev-server   - Set up development environment and run langgraph server"
	@echo "  make all          - Run lint, format, and test checks"
	@echo "  make help         - Show this help message" 