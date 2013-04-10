"""
test_input.py
unittesting for Input
"""

import unittest
from input import Input
from options import Options

class TestInput(unittest.TestCase):
    def test_input_stdin(self):
        Options.parse([])
        texts = Input.get_regexes()
        self.assertEqual(texts, ['a', 'a|b', 'ab', 'a*', 'a+', '[a-z]', '[^a-z]'])

