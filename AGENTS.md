# Repository Guidelines

## Project Structure & Module Organization
- `book_api/` holds FastAPI routers, Pydantic schemas, and SQLAlchemy models; follow the existing separation of CRUD helpers (`crud.py`), API wiring (`main.py`), and persistence (`database.py`).
- `tests/` mirrors public API behavior with pytest suites; add new feature coverage here before touching fixtures or shared utilities.
- `alembic/` wraps migrations and seed data (`data/books.json`); versioned scripts belong in `alembic/versions/` and should be generated through Alembic commands, not edited in place.

## Build, Test, and Development Commands
- `poetry install` prepares a local virtualenv with all dependencies.
- `make dev-run` starts the auto-reloading FastAPI server via `poetry run fastapi dev book_api/main.py` for iterative work.
- `make run` launches the production-style server.
- `make test` or `poetry run pytest` executes the full test suite.
- `poetry run alembic upgrade head` applies migrations; run after model changes or before seeding local data.

## Coding Style & Naming Conventions
- Stick to PEP 8 with 4-space indents; prefer explicit imports and keep modules under 300 lines.
- Use descriptive snake_case for functions, variables, and Alembic revisions; reserve PascalCase for Pydantic models and SQLAlchemy classes.
- Annotate public functions with type hints and return `schemas` objects from routers for consistent OpenAPI generation.

## Testing Guidelines
- Write pytest tests in files named `test_*.py`; group API tests by endpoint in `tests/test_books.py` or new modules under `tests/`.
- Aim to cover success and error flows; use HTTPX async clients or session fixtures where appropriate.
- Run `make test` before pushing; add regression tests whenever fixing bugs.

## Commit & Pull Request Guidelines
- Follow Conventional Commits (`fix:`, `docs:`, `chore(main): …`), as seen in the existing history.
- Keep commits focused; include schema or migration updates in the same change set that requires them.
- PRs should describe the problem, solution, and test evidence; link issues if available and mention any manual steps (e.g., `alembic upgrade head`).

## Database & Configuration Tips
- Default persistence uses SQLite (`books.db`); override via `SQLALCHEMY_DATABASE_URL` before app startup when targeting PostgreSQL.
- Enable a new migration with `poetry run alembic revision --autogenerate -m "describe change"`, review the script, then upgrade the head revision.
