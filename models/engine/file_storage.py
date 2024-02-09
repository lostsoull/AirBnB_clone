#!/usr/bin/python3
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

CLASSES = {"BaseModel": BaseModel,
           "User": User,
           "State": State,
           "City": City,
           "Amenity": Amenity,
           "Place": Place, 
           "Review": Review}

class FileStorage:
    """Used for storing data"""
    def __init__(self):
        FileStorage.__file_path = "file.json"
        FileStorage.__objects = {}

    def all(self):
        return FileStorage.__objects 
    
    def new(self, obj):
        FileStorage.__objects[obj.id f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        __objects_json = [key : obj.to_dict() for key, obj in self.__objects.items()]
        with open(self.__file_path, "w") as json_file:
            json.dumps(__objects_json, json_file)

    def reload(self):
        if os.path.exist(self.__file_path):
            with open(self.__file_path, "r") as json_file:
                data = json.load(json_file)
            FileStorage.__objects = [CLASSES[key.split(".")[0]](**value) for key, value in data.items()]

