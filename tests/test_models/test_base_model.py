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
        """

        my_id = "my-custom-id"
        custom_dt = datetime(2024, 5, 21, 12, 0, 0)
        bm = BaseModel(id=my_id, created_at=custom_dt, updated_at=custom_
