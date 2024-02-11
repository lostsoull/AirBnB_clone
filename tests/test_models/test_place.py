#!/usr/bin/python3
"""to import necessary modules"""
from models.place import Place
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """A testcase created by subclassing unittest;TestCase"""
    def test_class(self):
        """ Test the class"""
        my_model = Place()

        self.assertEqual(str(type(my_model)), "<class 'models.place.Place'>")

    def test_docstring(self):
        """ Test if docstring is correct"""

        self.assertIsNotNone(Place.__doc__)

    def test_Is_SubClass_BaseModel(self):
        """ Test the subclass of BaseModel"""

        self.assertTrue(issubclass(Place, BaseModel))

    def test_has_attr(self):
        """To test if user has all of its attributes"""
        my_model = Place()

        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertTrue(hasattr(my_model, 'city_code'))
        self.assertTrue(hasattr(my_model, 'user_code'))
        self.assertTrue(hasattr(my_model, 'name'))
        self.assertTrue(hasattr(my_model, 'description'))
        self.assertTrue(hasattr(my_model, 'room_count'))
        self.assertTrue(hasattr(my_model, 'bathroom_count'))
        self.assertTrue(hasattr(my_model, 'capacity'))
        self.assertTrue(hasattr(my_model, 'night_rate'))
        self.assertTrue(hasattr(my_model, 'location_latitude'))
        self.assertTrue(hasattr(my_model, 'location_longitude'))
        self.assertTrue(hasattr(my_model, 'amenities'))

    def test_type_attr(self):
        """ To test types of the attributes"""
        my_model = Place()

        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.city_id), str)
        self.assertEqual(type(my_model.user_id), str)
        self.assertEqual(type(my_model.name), str)
        self.assertEqual(type(my_model.description), str)
        self.assertEqual(type(my_model.number_rooms), int)
        self.assertEqual(type(my_model.number_bathrooms), int)
        self.assertEqual(type(my_model.max_guest), int)
        self.assertEqual(type(my_model.price_by_night), int)
        self.assertEqual(type(my_model.latitude), float)
        self.assertEqual(type(my_model.longitude), float)
        self.assertEqual(type(my_model.amenity_ids), list)

if __name__ == '__main__':
    unittest.main()
