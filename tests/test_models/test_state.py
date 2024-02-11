#!/usr/bin/python3
"""to import necessary modules"""
from models.state import State
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """A testcase created by subclassing unittest;TestCase"""
    def test_class(self):
        """ Test the class"""
        my_model = State()

        self.assertEqual(str(type(my_model)), "<class 'models.state.State'>")

    def test_docstring(self):
        """ Test if docstring is correct"""

        self.assertIsNotNone(State.__doc__)

    def test_Is_SubClass_BaseModel(self):
        """ Test the subclass of BaseModel"""

        self.assertTrue(issubclass(State, BaseModel))

    def test_has_attr(self):
        """To test if user has all of its attributes"""
        my_model = State()

        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertTrue(hasattr(my_model, 'name'))

    def test_type_attr(self):
        """ To test types of the attributes"""
        my_model = State()

        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.name), str)

if __name__ == '__main__':
    unittest.main()
