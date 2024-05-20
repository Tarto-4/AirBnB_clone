#!/usr/bin/python3

"""
Unit tests for the BaseModel class in models/base_model.py
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests functionality of the BaseModel class.
    """

    def test_new_instance(self):
        """
        Tests creating a new BaseModel instance with default attributes.
        """

        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertEqual(bm.created_at, bm.updated_at)

    def test_new_instance_with_kwargs(self):
        """
        Tests creating a new BaseModel instance with keyword arguments.

        We cannot directly pass a datetime object as a keyword argument
        in non-interactive mode (e.g., using echo and bash). As a workaround,
        we create a string representation of the desired datetime object
        and convert it back to datetime inside the test.
        """

        my_id = "my-custom-id"
        custom_dt_str = "2024-05-21 12:00:00"  # String representation of datetime
        bm = BaseModel(id=my_id, created_at=custom_dt_str, updated_at=custom_dt_str)

        # Convert string back to datetime object
        custom_dt = datetime.fromisoformat(custom_dt_str)

        self.assertEqual(bm.id, my_id)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertEqual(bm.created_at, custom_dt)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertEqual(bm.updated_at, custom_dt)  # Both created_at and updated_at should be equal

if __name__ == "__main__":
    unittest.main()
    
