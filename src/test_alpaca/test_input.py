"""
test_input.py
unittesting for Input
"""

import unittest
from alpacalib.input import Input
from alpacalib.options import Options

class TestInput(unittest.TestCase):
    def test_input_stdin(self):
        Options.parse([])
        texts = Input.get_regexes()
        self.assertEqual(texts, ['a', 'a|b', 'ab', 'a*', 'a+', '[a-z]', '[^a-z]'])

