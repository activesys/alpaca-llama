"""
test_options.py
unittesting for Options
"""

import unittest
from options import Options

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

