run:
	uvicorn src.api.main:app --reload

test:
	pytest -q

lint:
	ruff check .
