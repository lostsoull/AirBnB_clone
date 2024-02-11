#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Place

    the City.code
    the User.code
    name
    description
    rooms count
    bathrooms count
    number of guest
    price of night
    locate number
    locate number
    the list of Amenity.id later

    """
    city_code = ""
    user_code = ""
    name = ""
    description = ""
    room_count = 0
    bathroom_count = 0
    capacity = 0
    night_rate = 0
    location_latitude = 0.0
    location_longitude = 0.0
    amenities = []
