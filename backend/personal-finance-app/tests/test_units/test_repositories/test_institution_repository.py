import unittest
from unittest.mock import MagicMock, ANY

from pydantic import HttpUrl

from app.models.institution import Institution
from app.repositories.institution_repository import InstitutionRepository
from app.schemas.institution import InstitutionCreate


class TestInstitutionRepository(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.repo = InstitutionRepository(self.mock_db)

    def test_list_all(self):
        # Arrange
        expected_institutions = [Institution(id=1, name="Test Bank")]
        self.mock_db.query.return_value.all.return_value = expected_institutions

        # Act
        result = self.repo.list_all()

        # Assert
        self.mock_db.query.assert_called_once_with(Institution)
        self.assertEqual(result, expected_institutions)

    def test_get(self):
        # Arrange
        institution_id = 1
        expected_institution = Institution(id=institution_id, name="Test Bank")
        self.mock_db.query.return_value.filter.return_value.one_or_none.return_value = expected_institution

        # Act
        result = self.repo.get(institution_id)

        # Assert
        self.mock_db.query.assert_called_once_with(Institution)
        self.mock_db.query.return_value.filter.assert_called_once()
        self.assertEqual(result, expected_institution)

    def test_create(self):
        # Arrange
        inst_create = InstitutionCreate(
            name="New Bank",
            institution_type_id=1,
            website=HttpUrl("http://newbank.com")
        )

        # Act
        created_inst = self.repo.create(inst_create)

        # Assert
        self.mock_db.add.assert_called_once()
        self.mock_db.commit.assert_called_once()
        self.mock_db.refresh.assert_called_once()
        
        added_inst = self.mock_db.add.call_args[0][0]
        self.assertEqual(added_inst.name, inst_create.name)
        self.assertEqual(added_inst.website, str(inst_create.website))
        self.assertEqual(created_inst, added_inst)

    def test_update(self):
        # Arrange
        inst = Institution(id=1, name="Old Name")
        updates = {"name": "New Name", "website": HttpUrl("http://new.com/")}

        # Act
        updated_inst = self.repo.update(inst, updates)

        # Assert
        self.assertEqual(inst.name, "New Name")
        self.assertEqual(inst.website, "http://new.com/")
        self.mock_db.add.assert_called_once_with(inst)
        self.mock_db.commit.assert_called_once()
        self.mock_db.refresh.assert_called_once_with(inst)
        self.assertEqual(updated_inst, inst)