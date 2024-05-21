#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class Amenity that inherits from BaseModel

    Attributes:
        name: string - empty string (public class attribute)
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Creates a new Amenity instance

        Args:
            *args: Arguments passed to the parent class constructor
            **kwargs: Keyword arguments passed to the parent class constructor
        """
        super().__init__(self, *args, **kwargs)
