from app.models.transaction import Transaction


class TransactionRepository:
    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Transaction).all()

    def get(self, transaction_id: int):
        return self.db.query(Transaction).filter(Transaction.id == transaction_id).one_or_none()

    def create(self, tx_create):
        tx = Transaction(account_id=tx_create.account_id, amount=getattr(tx_create, 'amount', None), category=getattr(tx_create, 'category', None), transaction_type=getattr(tx_create, 'transaction_type', None), description=getattr(tx_create, 'description', None), related_account_id=getattr(tx_create, 'related_account_id', None))
        self.db.add(tx)
        self.db.commit()
        self.db.refresh(tx)
        return tx

    def update(self, tx: Transaction, updates: dict):
        for key, value in updates.items():
            if hasattr(tx, key) and value is not None:
                setattr(tx, key, value)
        self.db.add(tx)
        self.db.commit()
        self.db.refresh(tx)
        return tx

    def delete(self, tx: Transaction):
        self.db.delete(tx)
        self.db.commit()
        return None
