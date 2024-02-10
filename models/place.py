#!/usr/bin/python3
"""Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """This class is to manage place objects"""

    city_code = ""
    user_code = ""
    name = ""
    night_rate = 0
    rooms_count = 0
    bathrooms_count = 0
    capacity = 0      
    description = ""
    amenities = []
    location_latitude = 0.0
    location_longitude = 0.0
    amenities = []
