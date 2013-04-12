"""
test_regex.py
unittesting for Regex
"""

import unittest
import copy
from alpacalib.nfa import NFA
from alpacalib.graph import Graph
from alpacalib.regex import Regex
from alpacalib.regex import RegexError

class TestRegex(unittest.TestCase):
    def test_init(self):
        self.assertRaises(RegexError, Regex, '[ab-]')
    def test_transform(self):
        regex = Regex('(ab)+|[x-z]*')
        nfa = regex.transform()
        g1 = Graph()
        g1.new('a')
        g2 = Graph()
        g2.new('b')
        g3 = Graph()
        g3.new('x')
        g4 = Graph()
        g4.new('y')
        g5 = Graph()
        g5.new('z')

        g1.concatenation_graph(g2)
        g6 = copy.deepcopy(g1)
        g6.kleene_closure()
        g1.concatenation_graph(g6)
        g3.union_graph(g4)
        g3.union_graph(g5)
        g3.kleene_closure()
        g1.union_graph(g3)
        tnfa = NFA(g1)

        self.assertEqual(
            (nfa.graph.start, nfa.graph.finish, nfa.graph.adjlist),
            (tnfa.graph.start, tnfa.graph.finish, tnfa.graph.adjlist))

