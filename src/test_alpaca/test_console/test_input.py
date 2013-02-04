"""
test_input.py
"""

import unittest
from console import input

class TestFileInput(unittest.TestCase):
    def test_InvalidPathError(self):
        self.assertRaises(input.InvalidPathError, input.FileInput, '/home/wb/invalidpath/invalidfile')

    def test_iterator(self):
        with input.FileInput('./data/input.regex') as file_input:
            for line in file_input:
                self.assertEqual(line, 'test data in file input.regex')

class TestConsoleInput(unittest.TestCase):
    def test_iterator(self):
        with input.ConsoleInput() as console_input:
            for line in console_input:
                self.assertEqual(line, 'test data in stdin')

class TestInputFactory(unittest.TestCase):
    def test_create_fileinput(self):
        file_input = input.InputFactory().create('./data/input.regex')
        self.assertTrue(isinstance(file_input, input.FileInput))
        with file_input: pass

    def test_create_consoleinput(self):
        console_input = input.InputFactory().create('-')
        self.assertTrue(isinstance(console_input, input.ConsoleInput))

    def test_InvalidPathError(self):
        self.assertRaises(input.InvalidPathError, input.InputFactory().create, '/home/wb/invalidpath/invalidfile')

