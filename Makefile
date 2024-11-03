all: install format lint test

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black . --line-length 100 --verbose

lint:
	ruff check src/ --fix --verbose

test:
	python -m pytest -vv src/
	python -m pytest -vv --nbval *.ipynb || true

run:
	python src/main.py