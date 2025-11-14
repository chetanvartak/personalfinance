from app.repositories.budget_repository import BudgetRepository

class BudgetService:
    def __init__(self, db):
        self.repo = BudgetRepository(db)

    def list_budgets(self):
        return self.repo.list_all()
