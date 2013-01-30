"""
test_input.py
"""

import unittest
from console import input

class TestFileInput(unittest.TestCase):
    def test_FileInput_InvalidPathError(self):
        self.assertRaises(input.InvalidPathError, input.FileInput, '/home/wb/invalidpath/invalidfile')

    def test_FileInput_iterator(self):
        with input.FileInput('./data/input.regex') as file_input:
            for line in file_input:
                self.assertEqual(line, 'test data in file input.regex')

