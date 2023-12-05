#!/usr/bin/python3
"""
Module for BaseModel unit tests.
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ test the BaseModel class """
    def test_A_init(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
    
    def test_B_save(self):
        """ test save method """
        my_model = BaseModel()
        init_updated_at = my_model.updated_at
        curr_updated_at = my_model.save()
        self.assertNotEqual(init_updated_at, curr_updated_at)

    def test_C_to_dict(self):
        """ test to_dict method """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())
    def test_D_str(self):
        """ test __str__ method """
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

if __name__ == "__main__":
    unittest.main()