"""
test_nfa.py
unittesting for NFA
"""

import unittest
import copy
from nfa import NFA
from graph import Graph
from syntax import SyntaxParser
from regex import Regex

class TestNFA(unittest.TestCase):
    def test_init_empyt(self):
        nfa = NFA()
        self.assertEqual(nfa.graph, None)
    def test_init(self):
        graph = Graph()
        graph.new('a')
        nfa = NFA(graph)
        self.assertEqual(
            (nfa.graph.start, nfa.graph.finish, nfa.graph.adjlist),
            (graph.start, graph.finish, graph.adjlist))

    def test_merge_empty(self):
        nfa = NFA()
        l = []
        nfa.merge(l)
        self.assertEqual(nfa.graph, None)
    def test_merge(self):
        rs = ['a', 'bc', 'd|e', 'f*', 'g+', '[h-j]', '[^\\a-z]']
        nfas = [Regex(r).transform() for r in rs]
        nfa = NFA()
        nfa.merge(nfas)

        g = Graph()
        g1 = Graph()
        g1.new('a')
        g.union_graph(g1)
        g2 = Graph()
        g2.new('b')
        g3 = Graph()
        g3.new('c')
        g2.concatenation_graph(g3)
        g.union_graph(g2)
        g4 = Graph()
        g4.new('d')
        g5 = Graph()
        g5.new('e')
        g4.union_graph(g5)
        g.union_graph(g4)
        g6 = Graph()
        g6.new('f')
        g6.kleene_closure()
        g.union_graph(g6)
        g7 = Graph()
        g7.new('g')
        g8 = copy.deepcopy(g7)
        g8.kleene_closure()
        g7.concatenation_graph(g8)
        g.union_graph(g7)
        g9 = Graph()
        g9.new('h')
        g10 = Graph()
        g10.new('i')
        g11 = Graph()
        g11.new('j')
        g9.union_graph(g10)
        g9.union_graph(g11)
        g.union_graph(g9)
        g12 = Graph()
        g12.new('{')
        g13 = Graph()
        g13.new('|')
        g14 = Graph()
        g14.new('}')
        g15 = Graph()
        g15.new('~')
        g12.union_graph(g13)
        g12.union_graph(g14)
        g12.union_graph(g15)
        g.union_graph(g12)

        self.assertEqual(
            (nfa.graph.start, nfa.graph.finish, nfa.graph.adjlist),
            (g.start, g.finish, g.adjlist))

