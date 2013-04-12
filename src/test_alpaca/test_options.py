"""
test_options.py
unittesting for Options
"""

import unittest
from alpaca.options import Options
from alpaca.options import OptionsError

class TestOptions(unittest.TestCase):
    def test_get_input(self):
        Options.parse([])
        self.assertEqual(Options.get_input(), None)
        Options.parse(['input.regex'])
        self.assertEqual(Options.get_input(), 'input.regex')
    def test_get_output(self):
        Options.parse(['input.regex'])
        self.assertEqual(Options.get_output(), None)
        Options.parse(['-o output.gv', 'input.regex'])
        self.assertEqual(Options.get_output(), 'output.gv')
        Options.parse(['--output=output2.gv'])
        self.assertEqual(Options.get_output(), 'output2.gv')
        Options.parse(['--output', 'output3.gv'])
        self.assertEqual(Options.get_output(), 'output3.gv')
    def test_is_show_version(self):
        Options.parse([])
        self.assertFalse(Options.is_show_version())
        Options.parse(['-V'])
        self.assertTrue(Options.is_show_version())
        Options.parse(['--version'])
        self.assertTrue(Options.is_show_version())
    def test_is_show_help(self):
        Options.parse([])
        self.assertFalse(Options.is_show_help())
        Options.parse(['-h'])
        self.assertTrue(Options.is_show_help())
        Options.parse(['--help'])
        self.assertTrue(Options.is_show_help())
    def test_parse_error(self):
        self.assertRaises(OptionsError, Options.parse, ['-X'])

