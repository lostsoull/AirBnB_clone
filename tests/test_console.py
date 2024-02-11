#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on February 2024
@author: yassine abdourrabih and hanane zoubi
"""
import sys
import unittest
import inspect
import io
import pep8
from contextlib import redirect_stdout
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """to test HBNBCommand methods of the class"""

    @classmethod
    def setUpClass(cls):
        """Set up class method"""
        cls.setup = inspect.getmembers(HBNBCommand, inspect.isfunction)

    def test_pep8_conformance_HBNBCommand(self):
        """to test that console.py file conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/console.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_HBNBCommand(self):
        """To test that test_console.py file conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_console.py'])
        self.assertEqual(result.total_errors, 1,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """To test of module docstring documentation (exist)"""
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

    def test_class_docstring(self):
        """To test of class docstring documentation (exist)"""
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)
