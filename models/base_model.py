#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models in the project
    """

    def __init__(self, id=None, created_at=None, updated_at=None, **kwargs):
        """
        Initializes the base model

        Args:
            id (str, optional): Unique identifier for the object. Defaults to None.
            created_at (datetime, optional): Creation timestamp. Defaults to None.
            updated_at (datetime, optional): Update timestamp. Defaults to None.
            **kwargs (dict): Additional keyword arguments passed to the constructor.
        """
        self.id = id or str(uuid4())
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or self.created_at

        self.__dict__.update(kwargs)

    @staticmethod
    def from_dict(cls, dictionary):
        """
        Creates a new instance of the class from a dictionary

        Args:
            cls (class): The class to instantiate
            dictionary (dict): A dictionary containing the object attributes

        Returns:
            BaseModel: A new instance of the class with the attributes set from the dictionary
        """
        instance = cls(**dictionary)
        instance.id = instance.id or str(uuid4())
        instance.created_at = datetime.fromisoformat(dictionary.get('created_at'))
        instance.updated_at = datetime.fromisoformat(dictionary.get('updated_at'))
        return instance

    def save(self):
        """
        Updates the current datetime for updated_at and saves the object to storage
        """
        self.updated_at = datetime.now()
        FileStorage().save()

    def to_json(self):
        """
        Returns a dictionary representation of the object
        """
        return self.__dict__

    def __str__(self):
        """
        Returns a string representation of the object
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
