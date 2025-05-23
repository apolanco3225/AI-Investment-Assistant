install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C,E0401,E0611 *.py

all: install lint format 