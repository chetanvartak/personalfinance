from app.repositories.transaction_repository import TransactionRepository

class TransactionService:
    def __init__(self, db):
        self.repo = TransactionRepository(db)

    def list_transactions(self):
        return self.repo.list_all()
