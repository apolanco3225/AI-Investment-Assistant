install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C,E0401,E0611 *.py

test:
	pytest tests/ -v

test-coverage:
	pytest tests/ --cov=agent_tools -v

test-watch:
	pytest tests/ -v -f

all: install lint format test 