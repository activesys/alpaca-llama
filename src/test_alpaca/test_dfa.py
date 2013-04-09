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

    def test_minimize_only_one(self):
        g = Graph()
        g.new('a')
        self.dfa = DFA(copy.deepcopy(g))
        self.dfa.minimize()
        self.assertEqual((self.dfa.graph.start, self.dfa.graph.finish), (0, [1]))
        self.assertEqual(len(self.dfa.graph.adjlist), 2)
        self.assertEqual(len(self.dfa.graph.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.dfa.graph.adjlist[0])
        self.assertEqual(len(self.dfa.graph.adjlist[1]), 0)
    def test_minimize_mindfa(self):
        g = Graph()
        g.adjlist.extend([[(1, 'a'), (0, 'b')], [(1, 'a'), (2, 'b')], [(1, 'a'), (3, 'b')], [(1, 'a'), (0, 'b')]])
        g.start = 0
        g.finish = [3]
        self.dfa = DFA(copy.deepcopy(g))
        self.dfa.minimize()
        self.assertEqual((self.dfa.graph.start, self.dfa.graph.finish), (0, [3]))
        self.assertEqual(len(self.dfa.graph.adjlist), 4)
        self.assertEqual(len(self.dfa.graph.adjlist[0]), 2)
        self.assertIn((1, 'a'), self.dfa.graph.adjlist[0])
        self.assertIn((0, 'b'), self.dfa.graph.adjlist[0])
        self.assertEqual(len(self.dfa.graph.adjlist[1]), 2)
        self.assertIn((1, 'a'), self.dfa.graph.adjlist[1])
        self.assertIn((2, 'b'), self.dfa.graph.adjlist[1])
        self.assertEqual(len(self.dfa.graph.adjlist[2]), 2)
        self.assertIn((1, 'a'), self.dfa.graph.adjlist[2])
        self.assertIn((3, 'b'), self.dfa.graph.adjlist[2])
        self.assertEqual(len(self.dfa.graph.adjlist[3]), 2)
        self.assertIn((1, 'a'), self.dfa.graph.adjlist[3])
        self.assertIn((0, 'b'), self.dfa.graph.adjlist[3])
    def test_minimize(self):
        g = Graph()
        g.adjlist.extend([[(1, 'a'), (2, 'b')], [(1, 'a'), (3, 'b')], [(1, 'a'), (2, 'b')], [(1, 'a'), (4, 'b')], [(1, 'a'), (2, 'b')]])
        g.start = 0
        g.finish = [4]
        self.dfa = DFA(copy.deepcopy(g))
        self.dfa.minimize()
        self.assertEqual((self.dfa.graph.start, self.dfa.graph.finish), (0, [3]))
        self.assertEqual(len(self.dfa.graph.adjlist), 4)
        self.assertEqual(len(self.dfa.graph.adjlist[0]), 2)
        self.assertIn((1, 'a'), self.dfa.graph.adjlist[0])
        self.assertIn((0, 'b'), self.dfa.graph.adjlist[0])
        self.assertEqual(len(self.dfa.graph.adjlist[1]), 2)
        self.assertIn((1, 'a'), self.dfa.graph.adjlist[1])
        self.assertIn((2, 'b'), self.dfa.graph.adjlist[1])
        self.assertEqual(len(self.dfa.graph.adjlist[2]), 2)
        self.assertIn((1, 'a'), self.dfa.graph.adjlist[2])
        self.assertIn((3, 'b'), self.dfa.graph.adjlist[2])
        self.assertEqual(len(self.dfa.graph.adjlist[3]), 2)
        self.assertIn((1, 'a'), self.dfa.graph.adjlist[3])
        self.assertIn((0, 'b'), self.dfa.graph.adjlist[3])

