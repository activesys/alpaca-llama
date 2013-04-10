"""
test_output.py
unittesting for Output
"""

import unittest
from options import Options
from output import Output

class TestOutput(unittest.TestCase):
    def test_output_file(self):
        Options.parse(['--output=test_output_file.gv'])
        Output.output_script('digraph file {}')

