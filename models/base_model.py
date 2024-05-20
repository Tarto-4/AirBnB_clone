#!/usr/bin/python3

"""
This module defines the BaseModel class, which serves as the foundation for other models in your application.
It provides common attributes and methods for consistent data management.
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class providing common attributes (id, created_at, updated_at) and methods
    for other models to inherit.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args (optional): Unused positional arguments.
            **kwargs (dict, optional): Keyword arguments used to set attributes.
                - If provided, sets attributes based on key-value pairs.
                  Excludes the "__class__" key.
                - If not provided, creates a new instance with a unique ID,
                  current datetime for created_at and updated_at.

        Raises:
            ValueError: If both *args and **kwargs are provided.
        """

        if args and kwargs:
            raise ValueError("Received both positional and keyword arguments")

        if kwargs:
            self.__dict__.update((key, value) for key, value in kwargs.items() if key != "__class__")
            for key, value in self.__dict__.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.fromisoformat(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a human-readable string representation of the object,
        including class name, ID, and attributes as a dictionary.
        """

        return f"[{' '.join(self.__class__.__name__.split(' '))}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute of the object to the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the object into a dictionary representation,
        including all attributes and their values.

        Returns:
            dict: A dictionary representation of the object.
                - Includes a "__class__" key with the class name.
                - Converts "created_at" and "updated_at" to ISO format strings.
        """

        data = dict(self.__dict__)
        data["__class__"] = self.__class__.__name__
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
        return data
        
