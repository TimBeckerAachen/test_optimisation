install:
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	black src/*.py
	black tests/*.py

lint:
	pylint src/*.py

test:
	python -m pytest -vv --cov=src tests/