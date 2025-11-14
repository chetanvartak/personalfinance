#!/usr/bin/env bash
# Initialize the database (placeholder)
set -e

python - <<'PY'
from app.core.database import Base, engine
print('Creating database tables...')
Base.metadata.create_all(bind=engine)
print('Done')
PY
