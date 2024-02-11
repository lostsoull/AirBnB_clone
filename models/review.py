#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review

    """
    place_code = ""
    user_code = ""
    commentaire = ""
