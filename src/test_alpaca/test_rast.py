"""
test_rast.py
unittesting for RAST
"""

import unittest
from rast import RAST
from graph import Graph
from syntax import SyntaxParser

class TestRAST(unittest.TestCase):
    def test_is_empty(self):
        self.rast = RAST()
        self.assertTrue(self.rast.is_empty())

        self.syntax = SyntaxParser('a')
        self.rast = self.syntax.build()
        self.assertFalse(self.rast.is_empty())


