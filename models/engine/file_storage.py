#!/usr/bin/python3
"""Saving an object to a file
"""
from models.base_model import BaseModel
from models import amenity, city, place, review, state, user  # Import models directly
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes all objects in the storage to a JSON file"""
        objects_dict = {key: value.to_json() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserializes objects from a JSON file into the storage dictionary"""
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as file:
                objects_loaded = json.load(file)
                for key, value in objects_loaded.items():
                    class_name = value.get("__class__")
                    # Use getattr to dynamically access corresponding model class
                    model_class = getattr(sys.modules[__name__], class_name)
                    self.__objects[key] = model_class(**value)
        except FileNotFoundError:
            pass
            
