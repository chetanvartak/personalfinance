# Personal Finance App (microservice)

This is a FastAPI scaffold for a personal finance microservice. It provides a
skeleton for models, schemas, repositories, services, API endpoints, and tests.

How to run (development):

1. Create a virtualenv and activate it.

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows PowerShell
pip install -r requirements/base.txt
```

2. Initialize the database (uses SQLite by default):

```bash
python scripts/seed_data.py
```

3. Run the app:

```bash
uvicorn app.main:app --reload --port 8000 --env-file .env.dev
```

API root: http://localhost:8000/api/v1/

This repo contains placeholder implementations. Replace with production-ready
logic (password hashing, migrations, real database, tests, CI) before deploying.


SQLLite: Access DB
c:\sqlite3\sqlite3.exe C:\src\python\otherprojects\personalfinanace\backend\personal-finance-app\personal_finance.db

PostgresSQL: 
Export Schema
c:\Program Files\PostgreSQL\17\bin\pg_dump -U postgres -h localhost -p 5432 --schema-only personalfinance > C:\src\python\otherprojects\personalfinanace\backend\personal-finance-app\scripts\postgres_setup4.sql

Execute SQL
c:\Program Files\PostgreSQL\17\bin\psql  -U postgres -h localhost -p 5432 --schema personalfinance
