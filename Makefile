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

dev-deploy:
	langgraph dev

env-setup::
	uv venv .venv --python 3.11 && \
	. .venv/bin/activate && \
	uv pip install -e .

activate-env:
	source .venv/bin/activate

dev-server: env-setup dev-deploy

all: lint format test 

help:
	@echo "Available commands:"
	@echo "  make format        - Format Python code using black (src/*.py)"
	@echo "  make lint         - Run pylint checks on Python files (src/*.py)"
	@echo "  make test         - Run all tests with verbose output (tests/)"
	@echo "  make test-agents  - Run specific agent tests (tests/test_agents.py)"
	@echo "  make test-coverage - Run tests with coverage reporting for agent_tools"
	@echo "  make test-watch   - Run tests in watch mode (auto-rerun on changes)"
	@echo "  make install      - Create virtual environment and install package in editable mode"
	@echo "  make dev-deploy   - Start langgraph development server"
	@echo "  make env-setup    - Set up Python 3.11 virtual environment and install dependencies"
	@echo "  make dev-server   - Set up development environment and start langgraph server"
	@echo "  make all          - Run all checks: lint, format, and tests"
	@echo "  make help         - Display this help message" 