#!/usr/bin/python3
"""
Module that creates review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review that inherits from BaseModel

    Attributes:
        place_id (str): ID of the Place the review belongs to
        user_id (str): ID of the User who wrote the review
        text (str): Text content of the review
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Creates a new Review instance

        Args:
            *args: Arguments passed to the parent class constructor
            **kwargs: Keyword arguments passed to the parent class constructor
        """
        super().__init__(self, *args, **kwargs)

