#!/usr/bin/python3
"""
Module that creates users
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class representing a User
    """

    email = str
    password = str
    first_name = str
    last_name = str

    def __init__(self, *args, **kwargs):
        """
        Initializes the User object

        Args:
            *args (optional): Arguments passed to the parent class constructor
            **kwargs (dict): Keyword arguments for User attributes
        """
        super().__init__(self, *args, **kwargs)
