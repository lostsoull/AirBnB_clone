#!/usr/bin/python3
"""User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class is to manage city objects"""

    state_id = ""
    name = ""
