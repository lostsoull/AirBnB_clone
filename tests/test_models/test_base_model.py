#!/usr/bin/python3
"""to import necessary modules"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """A testcase created by subclassing unittest;TestCase"""
    def test_correct_instance(self):
        """ Test the class"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_obj_attributes(self):
        """test of instance"""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, '__init__'))
        self.assertTrue(hasattr(my_model, '__str__'))
        self.assertTrue(hasattr(my_model, 'save'))
        self.assertTrue(hasattr(my_model, 'to_dict'))

    def test_type_instance_datetime(self):
        """test created_at and updated_at"""
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_instance_attributes(self):
        """test of attributes"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89

        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(my_model.name, 'Holberton')
        self.assertEqual(type(my_model.name), str)
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(type(my_model.my_number), int)

    def test_unique_id(self):
        """test of unique id"""
        my_model = BaseModel()
        my_model2 = BaseModel()

        self.assertNotEqual(my_model.id, my_model2.id)

    def test_type_unique_id(self):
        """test of type of id"""
        my_model = BaseModel()

        self.assertEqual(type(my_model.id), str)

    def test_save_method(self):
        """test of save method"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        model_dict = my_model.to_dict()
        my_model.name = "School"
        my_model.save()
        model_dic2 = my_model.to_dict()

        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertEqual(model_dict['created_at'], model_dic2['created_at'])
        self.assertNotEqual(model_dict['updated_at'], model_dic2['updated_at'])
        self.assertEqual(my_model.__class__.__name__, model_dict['__class__'])
        self.assertEqual(my_model.id, model_dict['id'])
        self.assertEqual(my_model.name, model_dic2['name'])
        self.assertEqual(my_model.my_number, model_dict['my_number'])

    def test_to_dict_type(self):
        """is dict or not """
        my_model = BaseModel()
        tmp_dict_test = my_model.to_dict()

        self.assertEqual(type(tmp_dict_test), dict)

    def test_docstring(self):
        """Test Docstring"""

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_str_method(self):
        """ Test of str format"""
        my_model = BaseModel()

        test_string = "[{}] ({}) {}".format(my_model.__class__.__name__,
                                            my_model.id, my_model.__dict__)

        self.assertEqual(test_string, str(my_model))

    if __name__ == '__main__':
        unittest.main()
