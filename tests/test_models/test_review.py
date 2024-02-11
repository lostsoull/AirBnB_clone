#!/usr/bin/python3
""" Importing necessary modules """
from models.review import Review
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """A testcase created by subclassing unittest.TestCase. """
    def test_class(self):
        """ Test the class"""
        my_model = Review()

        self.assertEqual(str(type(my_model)), "<class 'models.review.Review'>")

    def test_docstring(self):
        """ Test if docstring is correct """

        self.assertIsNotNone(Review.__doc__)

    def test_Is_SubClass_BaseModel(self):
        """ Test the subclass of BaseModel"""

        self.assertTrue(issubclass(Review, BaseModel))

    def test_has_attr(self):
        """To test if user has all of its attributes """
        my_model = Review()

        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertTrue(hasattr(my_model, 'place_code'))
        self.assertTrue(hasattr(my_model, 'user_code'))
        self.assertTrue(hasattr(my_model, 'commentaire'))

    def test_type_attr(self):
        """ To test types of the attributes"""
        my_model = Review()

        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.place_code), str)
        self.assertEqual(type(my_model.user_code), str)
        self.assertEqual(type(my_model.commentaire), str)

if __name__ == '__main__':
    unittest.main()
