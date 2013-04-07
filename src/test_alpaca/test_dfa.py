"""
test_dfa.py
unittesting for DFA
"""

import unittest
import copy
from graph import Graph
from dfa import DFA

class TestDFA(unittest.TestCase):
    def test_init_empty(self):
        self.dfa = DFA()
        self.assertEqual(self.dfa.graph, None)
    def test_init(self):
        g = Graph()
        g.new('a')
        self.dfa = DFA(copy.deepcopy(g))
        self.assertEqual(
            (self.dfa.graph.start, self.dfa.graph.finish, self.dfa.graph.adjlist), 
            (g.start, g.finish, g.adjlist))

