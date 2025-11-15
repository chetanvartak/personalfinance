import unittest
from unittest.mock import MagicMock

from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryOut


class TestCategoryRepository(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.repo = CategoryRepository(self.mock_db)

    def test_list_all(self):
        # Arrange
        expected_categories = [Category(id=1, name="Groceries")]
        self.mock_db.query.return_value.all.return_value = expected_categories

        # Act
        result = self.repo.list_all()

        # Assert
        self.mock_db.query.assert_called_once_with(Category)
        self.assertEqual(result, expected_categories)

    def test_get(self):
        # Arrange
        category_id = 1
        expected_category = Category(id=category_id, name="Groceries")
        self.mock_db.query.return_value.filter.return_value.one_or_none.return_value = expected_category

        # Act
        result = self.repo.get(category_id)

        # Assert
        self.mock_db.query.assert_called_once_with(Category)
        self.assertEqual(result, expected_category)

    def test_create(self):
        # Arrange
        # The create method in CategoryRepository takes a payload with a 'name' attribute
        payload = MagicMock()
        payload.name = "Dining"

        # Act
        self.repo.create(payload)

        # Assert
        self.mock_db.add.assert_called_once()
        added_cat = self.mock_db.add.call_args[0][0]
        self.assertEqual(added_cat.name, "Dining")
        self.mock_db.commit.assert_called_once()