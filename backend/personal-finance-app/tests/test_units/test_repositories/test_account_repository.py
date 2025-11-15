from decimal import Decimal
import unittest
from unittest.mock import MagicMock

from app.models.account import Account
from app.repositories.account_repository import AccountRepository
from app.schemas.account import AccountCreate


class TestAccountRepository(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.repo = AccountRepository(self.mock_db)

    def test_list_all(self):
        # Arrange
        expected_accounts = [Account(id=1, account_name="Checking")]
        self.mock_db.query.return_value.all.return_value = expected_accounts

        # Act
        result = self.repo.list_all()

        # Assert
        self.mock_db.query.assert_called_once_with(Account)
        self.assertEqual(result, expected_accounts)

    def test_get(self):
        # Arrange
        account_id = 1
        expected_account = Account(id=account_id, account_name="Checking")
        self.mock_db.query.return_value.filter.return_value.one_or_none.return_value = expected_account

        # Act
        result = self.repo.get(account_id)

        # Assert
        self.mock_db.query.assert_called_once_with(Account)
        self.assertEqual(result, expected_account)

    def test_create(self):
        # Arrange
        account_create = AccountCreate(
            user_id=1,
            account_name="Savings",
            balance= Decimal("1000.00"),
            institution_id=1,
            account_type_id=1
        )

        # Act
        self.repo.create(account_create)

        # Assert
        self.mock_db.add.assert_called_once()
        added_account = self.mock_db.add.call_args[0][0]
        #self.assertEqual(added_account.account_name, "Savings")
        self.assertEqual(added_account.user_id, 1)
        self.mock_db.commit.assert_called_once()