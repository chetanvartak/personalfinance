from app.models.account import Account

class AccountRepository:
    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Account).all()
    
    def get(self, account_id: int):
        return self.db.query(Account).filter(Account.id == account_id).one_or_none()

    def create(self, account_create):
        # account_create may provide `name` (synonym for account_name)
        account = Account(user_id=account_create.user_id, account_name=account_create.account_name, account_number_last4=account_create.account_number_last4, balance=account_create.balance, opened_date=account_create.opened_date, currency=account_create.currency, status=account_create.status, institution_id=account_create.institution_id, account_type_id=account_create.account_type_id)
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account

    def update(self, account: Account, updates: dict):
        for key, value in updates.items():
            if hasattr(account, key) and value is not None:
                setattr(account, key, value)
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
        return account
    
    def delete(self, account: Account):
        self.db.delete(account)
        self.db.commit()
        return None
