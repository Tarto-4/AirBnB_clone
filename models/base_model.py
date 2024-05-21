#!/usr/bin/python3
from datetime import datetime
import uuid
from models.engine import file_storage
import models

class BaseModel:
    """A base class for all other models in the project"""

    id = str(uuid.uuid4())  # Generate a unique ID
    created_at = datetime.utcnow()  # Time of object creation
    updated_at = datetime.utcnow()  # Time of object update

    def __init__(self, *args, **kwargs):
        """
        Initializes the base model.
        - If args are not empty, assigns them to corresponding attributes.
        - If kwargs contains an "id" key, assigns it to the self.id attribute.
        - Otherwise, creates a new id and updates created_at and updated_at.
        - Calls storage.new(self) to add the object to the storage.
        """
        if args or kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "id" in kwargs:
                self.id = kwargs["id"]
            else:
                self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the object"""
        return f"[BaseModel] ({self.id}) {self.__class__.__name__}"

    def save(self):
        """Updates updated_at attribute and calls storage.save() to persist the object"""
        self.updated_at = datetime.utcnow()
        models.storage.save(self)

    def to_dict(self):
        """Returns a dictionary representation of the object"""
        object_dict = self.__dict__.copy()
        object_dict["created_at"] = object_dict["created_at"].isoformat()
        object_dict["updated_at"] = object_dict["updated_at"].isoformat()
        object_dict["__class__"] = self.__class__.__name__
        return object_dict
