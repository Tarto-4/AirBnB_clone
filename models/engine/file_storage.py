import json


class FileStorage:
    """
    Class for serializing and deserializing instances to and from a JSON file.
    """

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}  # Dictionary to store objects by <class name>.id

    def all(self):
        """
        Returns the dictionary __objects.
        """

        return self.__objects

    def new(self, obj):
        """
        Sets the obj in __objects with key <obj class name>.id.
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """

        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if it exists).
        """

        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    self.__objects[key] = self.instance(value)
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist

    @staticmethod
    def instance(data):
        """
        Returns a new instance of the class specified in the data dictionary.
        """

        class_name, id = data["__class__"], data["id"]
        del data["__class__"]
        del data["id"]
        return globals()[class_name](**data)  # Use globals() to retrieve the class


**models/__init__.py:**

```python
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
