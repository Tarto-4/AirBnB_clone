#!/usr/bin/python3
"""
Module that creates city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City that inherits from BaseModel

    Attributes:
        state_id: string - ID of the State the city belongs to (public class attribute)
        name: string - Name of the city (public class attribute)
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Creates a new City instance

        Args:
            *args: Arguments passed to the parent class constructor
            **kwargs: Keyword arguments passed to the parent class constructor
        """
        super().__init__(self, *args, **kwargs)
