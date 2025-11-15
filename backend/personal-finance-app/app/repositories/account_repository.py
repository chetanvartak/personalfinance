from typing import Optional

from sqlalchemy import Column
from sqlalchemy.orm import joinedload
from app.models.account import Account

class AccountRepository:
    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Account).options(joinedload(Account.institution), joinedload(Account.account_type)).all()
    
    def get(self, account_id: int):
        return self.db.query(Account).options(joinedload(Account.institution), joinedload(Account.account_type)).filter(Account.id == account_id).one_or_none()

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

    def search(
        self,
        institution_id: Optional[int] = None,
        account_type_id: Optional[int] = None,
        status: Optional[str] = None,
        currency: Optional[str] = None,
        account_name: Optional[str] = None,
    ):
        """
        Searches for accounts based on the given criteria.

        Args:
            institution_id: An optional institution ID to filter by.
            account_type_id: An optional account type ID to filter by.
            status: An optional status to filter by.
            currency: An optional currency to filter by.
            account_name: An optional account name to filter by (case-insensitive).
        """
        query = self.db.query(Account).options(joinedload(Account.institution), joinedload(Account.account_type))

        if institution_id is not None:
            query = query.filter(Account.institution_id == institution_id)

        if account_type_id is not None:
            query = query.filter(Account.account_type_id == account_type_id)

        if status is not None:
            query = query.filter(Account.status == status)

        if currency is not None:
            query = query.filter(Account.currency == currency)

        if account_name is not None:
            query = query.filter(Account.account_name.ilike(f"%{account_name}%"))

        return query.all()
