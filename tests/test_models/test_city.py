#!/usr/bin/python3
"""to mport necessary modules"""
from models.city import City
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """A testcase created by subclassing unittest;TestCase"""
    def test_class(self):
        """test the class"""
        my_model = City()

        self.assertEqual(str(type(my_model)), "<class 'models.city.City'>")

    def test_docstring(self):
        """ Test if docstring is correct"""

        self.assertIsNotNone(City.__doc__)

    def test_Is_SubClass_BaseModel(self):
        """ Test the subclass of BaseModel"""

        self.assertTrue(issubclass(City, BaseModel))

    def test_has_attr(self):
        """To test if user has all of its attributes """
        my_model = City()

        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertTrue(hasattr(my_model, 'state_id'))
        self.assertTrue(hasattr(my_model, 'name'))

    def test_type_attr(self):
        """ To test types of the attributes"""
        my_model = City()

        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.state_id), str)
        self.assertEqual(type(my_model.name), str)

if __name__ == '__main__':
    unittest.main()
