import csv
from datetime import datetime
from decimal import Decimal
from typing import IO, List

from app.repositories.transaction_repository import TransactionRepository
from app.schemas.transaction import TransactionCreate
from app.models.transaction import TransactionType

class TransactionService:
    def __init__(self, db):
        self.repo = TransactionRepository(db)

    def list_transactions(self):
        return self.repo.list_all()

    def import_from_csv(self, file: IO[str], account_id: int) -> List[TransactionCreate]:
        """
        Parses a CSV file and maps its rows to transaction objects.

        Assumes a CSV with the following columns:
        - Date (in YYYY-MM-DD format)
        - Description
        - Amount

        Args:
            file: A file-like object representing the CSV content.
            account_id: The ID of the account these transactions belong to.

        Returns:
            A list of Pydantic schemas for the transactions to be created.
        """
        reader = csv.DictReader(file)
        transactions_to_create: List[TransactionCreate] = []

        for row in reader:
            try:
                amount = Decimal(row["Amount"])
                transaction_date = datetime.strptime(row["Date"], "%Y-%m-%d")

                # Determine if it's a debit or credit
                transaction_type = 1 if amount < 0 else 2

                # Create a Pydantic model for validation and data consistency
                tx_create = TransactionCreate(
                    account_id=account_id,
                    date=transaction_date,
                    description=row["Description"],
                    amount=abs(amount),  # Store amount as a positive value
                    transaction_type_id=transaction_type,
                    # category_id can be set to a default or determined by rules
                    category_id=None,
                    related_account_id=None,
                )
                transactions_to_create.append(tx_create)
            except (KeyError, ValueError) as e:
                # Handle potential errors in CSV data (e.g., missing columns, bad date/amount format)
                print(f"Skipping row due to error: {row} - {e}")
                continue

        return transactions_to_create

    def save_imported_transactions(self, transactions_to_create: List[TransactionCreate]):
        """
        Saves a list of prepared transaction data to the database.
        """
        if not transactions_to_create:
            return []

        return self.repo.bulk_create(transactions_to_create)
