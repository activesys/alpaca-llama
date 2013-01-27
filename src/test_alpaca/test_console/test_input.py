"""
test_input.py
"""

import unittest
from console import input

class TestInput(unittest.TestCase):
    def setUp(self):
        self.input_data = input.Input('./data/input.regex')
    
    def test_iterator(self):
        for line in self.input_data:
            self.assertEqual(line, 'test data in file input.regex')

