#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        dict_obj = {}
        for key, obj in FileStorage.__objects.items():
            dict_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_obj, f)

    def reload(self):
        """Deserializes the JSON file to instances in __objects."""

        try:
            with open(self.__file_path, "r") as f:
                for key, value in json.load(f).items():
                    class_name = key.split(".")[0]
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
