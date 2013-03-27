"""
test_graph.py

unittesting for graph.
"""

import unittest
from graph import Graph
from graph import Vertex

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g = Graph()

    def test_new(self):
        self.g.new('a')
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        v, e = self.g.adjlist[0][0]
        self.assertEqual((v.index, v.state, e), (1, v.STATE_FINISH, 'a'))

        self.assertEqual(len(self.g.adjlist[1]), 0)

    def test_concatenation(self):
        self.g.concatenation('a')
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        v, e = self.g.adjlist[0][0]
        self.assertEqual((v.index, v.state, e), (1, v.STATE_FINISH, 'a'))

        self.assertEqual(len(self.g.adjlist[1]), 0)

        grap.concatenation('b')
        self.assertEqual((self.g.start, self.g.finish), (0, 2))
        self.assertEqual(len(self.g.adjlist), 3)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        v, e = self.g.adjlist[0][0]
        self.assertEqual((v.index, v.state, e), (1, v.STATE_IN_PROCESS, 'a'))

        self.assertEqual(len(self.g.adjlist[1]), 1)
        v, e = self.g.adjlist[1][0]
        self.assertEqual((v.index, v.state, e), (2, v.STATE_FINISH, 'b'))

        self.assertEqual(len(self.g.adjlist[2]), 0)

    def test_union(self):
        self.g.union('a')
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        v, e = self.g.adjlist[0][0]
        self.assertEqual((v.index, v.state, e), (1, v.STATE_FINISH, 'a'))

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.g.union('b')
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 4)

        self.assertEqual(len(self.g.adjlist[0]), 2)
        v, e = self.g.adjlist[0][0]
        self.assertEqual((v.index, v.state, e), (1, v.STATE_FINISH, 'a'))
        v, e = self.g.adjlist[0][1]
        self.assertEqual((v.index, v.state, e), (2, v.STATE_IN_PROCESS, ''))

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertEqual(len(self.g.adjlist[2]), 1)
        v, e = self.g.adjlist[2][0]
        self.assertEqual((v.index, v.state, e), (3, v.STATE_IN_PROCESS, 'b'))

        self.assertEqual(len(self.g.adjlist[3]), 1)
        v, e = self.g.adjlist[3][0]
        self.assertEqual((v.index, v.state, e), (1, v.STATE_FINISH, ''))

    def test_kleene_closure(self):
        self.g.new('a')
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        v, e = self.g.adjlist[0][0]
        self.assertEqual((v.index, v.state, e), (1, v.STATE_FINISH, 'a'))

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.g.kleen_closure()
        self.assertEqual((self.g.start, self.g.finish), (2, 3))
        self.assertEqual(len(self.g.adjlist), 4)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        v, e = self.g.adjlist[0][0]
        self.assertEqual((v.index, v.state, e), (1, v.STATE_IN_PROCESS, 'a'))

        self.assertEqual(len(self.g.adjlist[1]), 2)
        v, e = self.g.adjlist[1][0]
        self.assertEqual((v.index, v.state, e), (0, v.STATE_IN_PROCESS, ''))
        v, e = self.g.adjlist[1][1]
        self.assertEqual((v.index, v.state, e), (3, v.STATE_FINISH, ''))

        self.assertEqual(len(self.g.adjlist[2]), 2)
        v, e = self.g.adjlist[2][0]
        self.assertEqual((v.index, v.state, e), (0, v.STATE_IN_PROCESS, ''))
        v, e = self.g.adjlist[2][1]
        self.assertEqual((v.index, v.state, e), (3, v.STATE_FINISH, ''))

        self.assertEqual(len(self.g.adjlist[3]), 0)

    def test_new_graph(self):
        pass
    def test_concatenation_graph(self):
        pass
    def test_union_graph(self):
        pass
    def test_kleene_closure_graph(self):
        pass
