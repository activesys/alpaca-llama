"""
test_nfa.py
unittesting for NFA
"""

import unittest
from nfa import NFA
from graph import Graph
from syntax import SyntaxParser

class TestNFA(unittest.TestCase):
    def test_init_empyt(self):
        nfa = NFA()
        self.assertEqual(nfa.graph, None)
    def test_init(self):
        graph = Graph()
        graph.new('a')
        nfa = NFA(graph)
        self.assertEqual(nfa.graph, graph)

