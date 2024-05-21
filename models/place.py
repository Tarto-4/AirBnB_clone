#!/usr/bin/python3
"""
Module that creates place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class representing a Place
    """

    city_id = str
    user_id = str
    name = str
    description = str
    number_rooms = int
    number_bathrooms = int
    max_guest = int
    price_by_night = int
    latitude = float
    longitude = float
    amenity_ids = list

    def __init__(self, *args, **kwargs):
        """
        Initializes the Place object

        Args:
            *args (optional): Arguments passed to the parent class constructor
            **kwargs (dict): Keyword arguments for Place attributes
        """
        super().__init__(self, *args, **kwargs)
