"""
test_options.py
"""

import unittest
from console import options

class TestOptions(unittest.TestCase):
    def test_input_file(self):
        args = 'input.regex'.split()
        input_option = options.Options(args)
        self.assertEqual(input_option.input_path, 'input.regex')

    def test_input_console(self):
        input_option = options.Options()
        self.assertEqual(input_option.input_path, '-')

    def test_output_file(self):
        args = '-o output.dot'.split()
        output_option = options.Options(args)
        self.assertEqual(output_option.output_path, 'output.dot')

    def test_output_console(self):
        output_option = options.Options()
        self.assertEqual(output_option.output_path, '-')

