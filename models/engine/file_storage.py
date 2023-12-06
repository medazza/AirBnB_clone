#!/usr/bin/python3
"""
Module for serialize and deserialize data(dict <-> json)
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
import json
import os

class FileStorage():
    """
    FileStorage class for storing, serialize 
    and deserialize data
    """
    __file_path = "file.json"
    __objects = dict()

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj


    def all(self):
        """
        returns the dictionary __objects
        """
        return  FileStorage.__objects


    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        all_objects = FileStorage.__objects
        obj_dict = dict()
        for obj in all_objects.keys():
            obj_dict[obj] = all_objects[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    dict_obj = json.load(f)
                    for k, v in dict_obj.items():
                        class_name, obj_id = k.split('.')
                        cls = eval(class_name)
                        instance = cls(**v)
                        FileStorage.__objects[k] = instance
                except Exception:
                    pass
