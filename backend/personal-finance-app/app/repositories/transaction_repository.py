from datetime import date, datetime
from typing import List, Optional

from sqlalchemy import asc, desc
from app.schemas.transaction import TransactionCreate
from app.models.transaction import Transaction
from sqlalchemy.orm import joinedload

class TransactionRepository:
    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Transaction).options(
            joinedload(Transaction.account),
            joinedload(Transaction.category),
            joinedload(Transaction.transaction_type),
            joinedload(Transaction.related_account)
        ).all()

    def get(self, transaction_id: int):
        return self.db.query(Transaction).options(
            joinedload(Transaction.account),
            joinedload(Transaction.category),
            joinedload(Transaction.transaction_type),
            joinedload(Transaction.related_account)
        ).filter(Transaction.id == transaction_id).one_or_none()

    def create(self, tx_create):
        tx = Transaction(account_id=tx_create.account_id, amount=tx_create.amount, category_id=tx_create.category_id, date=tx_create.date, transaction_type_id=tx_create.transaction_type_id, description=tx_create.description, related_account_id=tx_create.related_account_id)
        self.db.add(tx)
        self.db.commit()
        self.db.refresh(tx)
        return tx

    def bulk_create(self, transactions_to_create: List[TransactionCreate]) -> List[Transaction]:
        """
        Creates multiple transactions in a single database session.

        Args:
            transactions_to_create: A list of transaction creation schemas.

        Returns:
            A list of the created transaction objects.
        """
        transactions = [Transaction(**tx.model_dump()) for tx in transactions_to_create]
        # Add each transaction individually

        self.db.add_all(transactions)
        
        self.db.commit()
        # Note: self.db.refresh() does not work on a list.
        # The objects in the 'transactions' list are updated with IDs by SQLAlchemy.
        return transactions

    def update(self, tx: Transaction, updates: dict):
        for key, value in updates.items():
            if hasattr(tx, key) and value is not None:
                setattr(tx, key, value)
        self.db.add(tx)
        self.db.commit()
        self.db.refresh(tx)
        return tx

    def search(
        self,
        start_date: datetime,
        end_date: datetime,
        account_ids: Optional[List[int]] = None,
        category_ids: Optional[List[int]] = None,
        description: Optional[str] = None,
    ):
        """
        Searches for transactions based on the given criteria.

        Args:
            start_date: The start of the date range (inclusive).
            end_date: The end of the date range (inclusive).
            account_ids: An optional list of account IDs to filter by.
            category_ids: An optional list of category IDs to filter by.
            description: An optional description pattern to filter by (case-insensitive).

        Returns:
            A list of transactions matching the criteria.
        """
        query = self.db.query(Transaction)

        # 1. Date Range (Required)
        query = query.filter(Transaction.date.between(start_date, end_date))

        # 2. Optional Account IDs
        if account_ids:
            query = query.filter(Transaction.account_id.in_(account_ids))

        # 3. Optional Description (ILIKE comparison)
        if description:
            query = query.filter(Transaction.description.ilike(f"%{description}%"))

        # 4. Optional Category IDs
        if category_ids:
            query = query.filter(Transaction.category_id.in_(category_ids))

        return query.options(
            joinedload(Transaction.account),
            joinedload(Transaction.category),
            joinedload(Transaction.transaction_type),
            joinedload(Transaction.related_account)
        ).all()

    def delete(self, tx: Transaction):
        self.db.delete(tx)
        self.db.commit()
        return None

    def list_filtered_transactions(self, page: int, page_size: int, sort_by: str, sort_order: str, search: Optional[str] = None, account_id: Optional[int] = None, category_id: Optional[int] = None, date_from: Optional[datetime] = None, date_to: Optional[datetime] = None):
        query = self.db.query(Transaction).options(
            joinedload(Transaction.account),
            joinedload(Transaction.category),
            joinedload(Transaction.transaction_type),
            joinedload(Transaction.related_account)
        )

        # Filtering
        if search:
            query = query.filter(Transaction.description.ilike(f"%{search}%"))
        if account_id:
            query = query.filter(Transaction.account_id == account_id)
        if category_id:
            query = query.filter(Transaction.category_id == category_id)
        if date_from:
            query = query.filter(Transaction.date >= date_from)
        if date_to:
            query = query.filter(Transaction.date <= date_to)

        # Sorting
        sort_column = getattr(Transaction, sort_by)
        if sort_order == "desc":
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        total = query.count()
        items = query.offset((page - 1) * page_size).limit(page_size).all()
        return {
            "transactions": items,
            "total": total,
            "page": page,
            "page_size": page_size
        }   