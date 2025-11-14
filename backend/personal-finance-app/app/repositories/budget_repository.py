from app.models.budget import Budget

class BudgetRepository:
    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Budget).all()
