#!/usr/bin/python3
"""Import necessary modules """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """where the classes will inherit """
    def __init__(self, *args, **kwargs):
        """ Constructor method """
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """the string representation of class name, id and dict"""
        class_name = str("[" + self.__class__.__name__ + "]")
        instance_id = str("(" + self.id + ")")
        instance_dict = str(self.__dict__)
        return (class_name + " " + instance_id + " " + instance_dict)

    def save(self):
        
        """Updates the public instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """a dictionary containing all values of instance """
        dict_objs = {}
        tmp_var = self.__dict__

        for key, values in tmp_var.items():
            if key == 'created_at' or key == 'updated_at':
                dict_objs[key] = values.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                if not values:
                    pass
                else:
                    dict_objs[key] = values
        dict_objs['__class__'] = self.__class__.__name__

        return (dict_objs)
