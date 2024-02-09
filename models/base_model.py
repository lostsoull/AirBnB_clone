#!/usr/bin/python3
"""Module for BaseModel class."""
from models import storage
from datetime import datetime
import uuid

class BaseModel:
    """BaseModel class with custom attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = self.updated_at = kwargs.get('created_at', datetime.now())

        if kwargs:
            for key, value in kwargs.items():
                if key not in ["__class__", "id", "created_at"]:
                    setattr(self, key, value)
        storage.new(self)

    def __str__(self):
        """Return string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute last_update with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary representation of the BaseModel instance."""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_dict = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key not in ["id", "created_at"]:
                obj_dict[key] = value

        obj_dict['id'] = self.id
        obj_dict['created_at'] = self.created_at.strftime(date_format)
        obj_dict['updated_at'] = self.updated_at.strftime(date_format)
        return obj_dict

