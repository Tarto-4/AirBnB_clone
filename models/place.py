#!/usr/bin/python3
"""
Module that creates place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Place that inherits from BaseModel

    Attributes:
        city_id: str - ID of the City the place belongs to (public class attribute)
        user_id: str - ID of the User who owns the place (public class attribute)
        name: str - Name of the place (public class attribute)
        description: str - Description of the place (public class attribute)
        number_rooms: int - Number of rooms in the place (public class attribute)
        number_bathrooms: int - Number of bathrooms in the place (public class attribute)
        max_guest: int - Maximum number of guests allowed in the place (public class attribute)
        price_by_night: int - Price per night for the place (public class attribute)
        latitude: float - Latitude coordinate of the place (public class attribute)
        longitude: float - Longitude coordinate of the place (public class attribute)
        amenity_ids: list[str] - List of Amenity.id strings associated with the place (public class attribute)
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids: list[str] = []

    def __init__(self, *args, **kwargs):
        """
        Creates a new Place instance

        Args:
            *args: Arguments passed to the parent class constructor
            **kwargs: Keyword arguments passed to the parent class constructor
        """
        super().__init__(self, *args, **kwargs)
