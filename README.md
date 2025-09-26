# Book API

Book API is a FastAPI-powered service that provides CRUD endpoints for managing a small
collection of books. It uses SQLAlchemy for persistence and ships with an Alembic
migration that seeds the database with a demo dataset.

## Features

- List books with pagination-ready helpers.
- Retrieve individual books by identifier.
- Create, update, and delete books through RESTful endpoints.
- SQLite persistence configured via SQLAlchemy with Alembic migrations.

## Getting Started

1. Install dependencies using [Poetry](https://python-poetry.org/):
   ```bash
   poetry install
   ```
2. Apply the database migrations:
   ```bash
   poetry run alembic upgrade head
   ```
3. Start the FastAPI application:
   ```bash
   poetry run uvicorn book_api.main:app --reload
   ```

The API will be served at `http://127.0.0.1:8000`. Interactive documentation is
available at `/docs`.

## Running Tests

Execute the automated tests with:

```bash
poetry run pytest
```

## Project Structure

- `book_api/` – Application modules including routers, schemas, and database setup.
- `alembic/` – Database migrations and seed data.
- `tests/` – Automated test suite for the API.

## License

This project is distributed under the terms of the MIT License.
