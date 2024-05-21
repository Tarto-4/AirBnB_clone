#!/usr/bin/python3
"""
A module for Ammenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class representing an Amenity
    """

    name = str

    def __init__(self, *args, **kwargs):
        """
        Initializes the Amenity object

        Args:
            *args (optional): Arguments passed to the parent class constructor
            **kwargs (dict): Keyword arguments for Amenity attributes
        """
        super().__init__(self, *args, **kwargs)
