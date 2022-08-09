install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_awscli.py

format:
	black *.py

lint:
	pylint --disable=R,C awscli.py

all: install lint test format