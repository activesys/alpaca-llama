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

    def test_move_empyt(self):
        nfa = Regex('a*|ab').transform()
        self.assertEqual(nfa._NFA__move(set(), 'a'), set())
    def test_move_invalid_edge(self):
        nfa = Regex('a*|ab').transform()
        self.assertEqual(nfa._NFA__move({0, 4, 6}, 'c'), set())
    def test_move(self):
        nfa = Regex('a*|ab').transform()
        self.assertEqual(nfa._NFA__move({0, 4, 6}, 'a'), {1, 5})

    def test_epsilon_closure_no_epsilon(self):
        nfa = Regex('abc').transform()
        self.assertEqual(nfa._NFA__epsilon_closure({0}), {0})
    def test_epsilon_closure_union(self):
        nfa = Regex('a|b|c').transform()
        self.assertEqual(nfa._NFA__epsilon_closure({0}), {0, 2, 4})
    def test_epsilon_closure(self):
        g1 = Graph()
        g1.new('a')
        g2 = Graph()
        g2.new('b')
        g2.union('c')
        g1.union_graph(g2)
        nfa = NFA(g1)
        self.assertEqual(nfa._NFA__epsilon_closure({0}), {0, 2, 4})

