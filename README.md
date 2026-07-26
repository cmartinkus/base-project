# base-project
Base project for a scientific application with an api, ui, postgres database, message queue, and scientific processing services

#makefile
sync:
	uv sync

api:
	uv run --package company-api-service uvicorn api_service.main:app --reload

worker:
	uv run --package company-python-service python -m python_service.main

test:
	uv run pytest