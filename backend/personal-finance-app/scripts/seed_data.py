"""Seed minimal demo data into the database (placeholder).
Run: python scripts/seed_data.py

This script adjusts sys.path so it can be executed directly from the project
root (or from the scripts folder) without needing to install the package.
If you prefer, run the script as a module from the project root:

    python -m scripts.seed_data

"""
from pathlib import Path
import sys

# Ensure project root is on sys.path so `import app` works when running the script
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.core.database import Base, engine, SessionLocal
from app.models.user import User
from app.models.account import Account  # noqa: F401 to register the model  


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if not db.query(User).first():
            u = User(username='demo', email='demo@example.com', hashed_password='not_hashed')
            db.add(u)
            db.commit()
            print('Inserted demo user')
        else:
            print('Demo data already present')
    finally:
        db.close()

    try:
        if not db.query(Account).first():
            a = Account(name='demo_account', user_id=1)
            db.add(a)
            db.commit()
            print('Inserted demo account')
        else:
            print('Demo data already present')
    finally:
        db.close()        


if __name__ == '__main__':
    seed()
