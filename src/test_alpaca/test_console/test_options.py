"""
test_options.py
"""

import unittest
from console import options

class TestOptions(unittest.TestCase):
    def test_register_error(self):
        args = '-a -b -c d'.split()
        self.assertRaises(options.OptionsInvalidError, options.Options().register, args)

    def test_input_file(self):
        args = 'input.regex'.split()
        options.Options().register(args)
        self.assertEqual(options.Options().input_file(), 'input.regex')

    def test_input_console(self):
        options.Options().register()
        self.assertEqual(options.Options().input_file(), '-')

    def test_output_file(self):
        args = '-o output.dot'.split()
        options.Options().register(args)
        self.assertEqual(options.Options().output_file(), 'output.dot')

    def test_output_console(self):
        options.Options().register()
        self.assertEqual(options.Options().output_file(), '-')

    def test_io_file(self):
        args = '-o output.dot input.regex'.split()
        options.Options().register(args)
        self.assertEqual(options.Options().input_file(), 'input.regex')
        self.assertEqual(options.Options().output_file(), 'output.dot')

    def test_i_file_o_console(self):
        args = 'input.regex'.split()
        options.Options().register(args)
        self.assertEqual(options.Options().input_file(), 'input.regex')
        self.assertEqual(options.Options().output_file(), '-')

    def test_i_console_o_file(self):
        args = '-o output.dot'.split()
        options.Options().register(args)
        self.assertEqual(options.Options().input_file(), '-')
        self.assertEqual(options.Options().output_file(), 'output.dot')

    def test_io_console(self):
        options.Options().register()
        self.assertEqual(options.Options().input_file(), '-')
        self.assertEqual(options.Options().output_file(), '-')

