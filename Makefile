.PHONY: pre-commit

install:
	pip install -r requirements.txt

pre-commit:
	pre-commit run --all-files

test:
	@export PYTHONPATH="/home/bexon/Desktop/ztm-warsaw-research/src"; \
	pytest -v --cov=src --cov-report=term-missing --cov-fail-under=100 tests/
