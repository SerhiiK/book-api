.PHONY: run

dev-run:
	poetry run fastapi dev book_api/main.py

run:
	poetry run fastapi run book_api/main.py

test:

