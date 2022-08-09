install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv test_awscli.py

lint:
	pylint --disable=R,C awscli.py awslib

all: install lint test format