#!/usr/bin/python3
"""Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This class is to manage review objects"""

    place_code = ""
    user_code = ""
    commentaire = ""
