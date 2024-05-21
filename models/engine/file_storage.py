#!/usr/bin/python3
import json

class FileStorage:
    """A class to serialize and deserialize BaseModels to/from a JSON file"""

    __file_path: str = "file.json"  # Path to the JSON file
    __objects: dict = {}  # Dictionary to hold objects (key: class name.id, value: object)

    def all(self) -> dict:
        """Returns the dictionary of all stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes all objects in the storage to a JSON file"""
        objects_dict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            import json

            json.dump(objects_dict, file)

    def reload(self):
        """Deserializes objects from a JSON file into the storage dictionary"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                import json

                objects_dict = json.load(file)
                from models.base_model import BaseModel

                FileStorage.__objects = {
                    key: BaseModel(**value) for key, value in objects_dict.items()
                }
        except FileNotFoundError:
            pass  # Ignore if file doesn'  t exist
