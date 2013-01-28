"""
test_output.py
"""

import unittest
from console import output

class TestOutput(unittest.TestCase):
    def setUp(self):
        self.output = output.Output('./data/output.dot')

    def test_output(self):
        script = 'abcdefghijklmnopqrstuvwxyz\nABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.output.output(script)
        dot_file = open('./data/output.dot', 'r')
        temp = dot_file.read()
        dot_file.close()
        self.assertEqual(script, temp)
