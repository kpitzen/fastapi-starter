.PHONY=lint

lint:
	poetry run isort --recursive --diff --quiet --check src tests
	poetry run mypy --config-file .mypy.ini src tests
	poetry run bandit -r src
	poetry run black --diff --check --verbose src tests

format:
	poetry run isort -rc --atomic .
	poetry run black --verbose src tests

serve:
	poetry run uvicorn api.app:app --reload
