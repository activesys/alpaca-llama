"""
test_input.py
unittesting for Input
"""

import unittest
from alpaca.input import Input
from alpaca.options import Options

class TestInput(unittest.TestCase):
    def test_input_stdin(self):
        Options.parse([])
        texts = Input.get_regexes()
        self.assertEqual(texts, ['a', 'a|b', 'ab', 'a*', 'a+', '[a-z]', '[^a-z]'])

