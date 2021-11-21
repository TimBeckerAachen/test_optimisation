install:
	pipenv install

format:
	black src/*.py
	black tests/*.py

lint:
	pylint src/*.py

test:
	python -m pytest -vv --cov=src tests/