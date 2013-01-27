"""
test_options.py
"""

import unittest
from console import options

class TestOptions(unittest.TestCase):
    def setUp(self):
        args = '-o output.dot input.regex'.split()
        self.options = options.Options(args)

    def test_input_path(self):
        self.assertEqual(self.options.input_path, 'input.regex')

    def test_output_path(self):
        self.assertEqual(self.options.output_path, 'output.dot')

