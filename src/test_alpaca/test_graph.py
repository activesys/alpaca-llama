"""
test_graph.py

unittesting for graph.
"""

import unittest
from graph import Graph
from graph import Vertex
from graph import GraphNonEmptyError

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g = Graph()

    def test_new(self):
        self.g.new('a')
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertRaises(GraphNonEmptyError, self.g.new, 'b')

    def test_concatenation(self):
        self.g.concatenation('a')
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.g.concatenation('b')
        self.assertEqual((self.g.start, self.g.finish), (0, 2))
        self.assertEqual(len(self.g.adjlist), 3)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_IN_PROCESS), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((Vertex(2, Vertex.STATE_FINISH), 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 0)

    def test_union(self):
        self.g.union('a')
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.g.union('b')
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 4)

        self.assertEqual(len(self.g.adjlist[0]), 2)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), 'a'), self.g.adjlist[0])
        self.assertIn((Vertex(2, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((Vertex(3, Vertex.STATE_IN_PROCESS), 'b'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), ''), self.g.adjlist[3])

    def test_kleene_closure(self):
        self.g.new('a')
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.g.kleen_closure()
        self.assertEqual((self.g.start, self.g.finish), (2, 3))
        self.assertEqual(len(self.g.adjlist), 4)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_IN_PROCESS), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 2)
        self.assertIn((Vertex(0, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[1])
        self.assertIn((Vertex(3, Vertex.STATE_FINISH), ''), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 2)
        self.assertIn((Vertex(0, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[2])
        self.assertIn((Vertex(3, Vertex.STATE_FINISH), ''), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 0)

    def test_new_graph(self):
        graph = Graph()
        graph.new('a')
        self.g.new_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)


    def test_concatenation_graph(self):
        graph = Graph()
        self.g.new('a')
        self.g.concatenation_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        graph.new('b')
        self.g.concatenation_graph(graph)
        self.assertEqual((self.g.start, self.g.finish), (0, 2))
        self.assertEqual(len(self.g.adjlist), 3)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_IN_PROCESS), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((Vertex(2, Vertex.STATE_IN_PROCESS), 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 0)

    def test_concatenation_graph_union_kleene(self):
        self.g.new('a')
        self.g.union('b')
        graph = Graph()
        graph.new('c')
        graph.kleen_closure()
        self.g.concatenation_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, 7))
        self.assertEqual(len(self.g.adjlist), 8)

        self.assertEqual(len(self.g.adjlist[0]), 2)
        self.assertIn((Vertex(1, Vertex.STATE_IN_PROCESS), 'a'), self.g.adjlist[0])
        self.assertIn((Vertex(2, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((Vertex(6, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((Vertex(3, Vertex.STATE_IN_PROCESS), 'b'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 1)
        self.assertIn((Vertex(5, Vertex.STATE_IN_PROCESS), 'c'), self.g.adjlist[4])

        self.assertEqual(len(self.g.adjlist[5]), 2)
        self.assertIn((Vertex(4, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[5])
        self.assertIn((Vertex(7, Vertex.STATE_FINISH), ''), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 2)
        self.assertIn((Vertex(4, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[6])
        self.assertIn((Vertex(7, Vertex.STATE_FINISH), ''), self.g.adjlist[6])

        self.assertEqual(len(self.g.adjlist[7]), 0)

    def test_concatenation_graph_concatenation_kleene(self):
        self.g.new('a')
        self.g.concatenation('b')
        graph = Graph()
        graph.new('c')
        graph.kleen_closure()
        self.g.concatenation_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, 6))
        self.assertEqual(len(self.g.adjlist), 7)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_IN_PROCESS), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((Vertex(2, Vertex.STATE_IN_PROCESS), 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((Vertex(5, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((Vertex(4, Vertex.STATE_IN_PROCESS), 'c'), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 2)
        self.assertIn((Vertex(3, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[4])
        self.assertIn((Vertex(6, Vertex.STATE_FINISH), ''), self.g.adjlist[4])

        self.assertEqual(len(self.g.adjlist[5]), 2)
        self.assertIn((Vertex(3, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[5])
        self.assertIn((Vertex(6, Vertex.STATE_FINISH), ''), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 0)

    def test_concatenation_graph_concatenation_union(self):
        self.g.new('a')
        self.g.concatenation('b')
        graph = Graph()
        graph.new('c')
        graph.union('d')
        self.g.concatenation_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, 4))
        self.assertEqual(len(self.g.adjlist), 7)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_IN_PROCESS), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((Vertex(2, Vertex.STATE_IN_PROCESS), 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((Vertex(3, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((Vertex(4, Vertex.STATE_FINISH), 'c'), self.g.adjlist[3])
        self.assertIn((Vertex(5, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 0)

        self.assertEqual(len(self.g.adjlist[5]), 1)
        self.assertIn((Vertex(6, Vertex.STATE_IN_PROCESS), 'd'), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 1)
        self.assertIn((Vertex(4, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[6])

    def test_union_graph_union_concatenation(self):
        self.g.new('a')
        self.g.union('b')
        graph = Graph()
        graph.new('c')
        graph.concatenation('d')
        self.g.union_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, 2))
        self.assertEqual(len(self.g.adjlist), 7)

        self.assertEqual(len(self.g.adjlist[0]), 2)
        self.assertIn((Vertex(1, Vertex.STATE_IN_PROCESS), 'a'), self.g.adjlist[0])
        self.assertIn((Vertex(3, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((Vertex(2, Vertex.STATE_FINISH), 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 0)

        self.assertEqual(len(self.g.adjlist[3]), 2)
        self.assertIn((Vertex(4, Vertex.STATE_IN_PROCESS), 'c'), self.g.adjlist[3])
        self.assertIn((Vertex(5, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 1)
        self.assertIn((Vertex(2, Vertex.STATE_FINISH), ''), self.g.adjlist[4])

        self.assertEqual(len(self.g.adjlist[5]), 1)
        self.assertIn((Vertex(6, Vertex.STATE_IN_PROCESS), 'd'), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 1)
        self.assertIn((Vertex(4, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[6])

    def test_union_graph_concatenation_kleene(self):
        self.g.new('a')
        self.g.concatenation('b')
        graph = Graph()
        graph.new('c')
        graph.kleen_closure()
        self.g.union_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, 2))
        self.assertEqual(len(self.g.adjlist), 7)

        self.assertEqual(len(self.g.adjlist[0]), 2)
        self.assertIn((Vertex(1, Vertex.STATE_IN_PROCESS), 'a'), self.g.adjlist[0])
        self.assertIn((Vertex(5, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((Vertex(2, Vertex.STATE_FINISH), 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 0)

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((Vertex(4, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 2)
        self.assertIn((Vertex(3, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[4])
        self.assertIn((Vertex(6, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[4])

        self.assertEqual(len(self.g.adjlist[5]), 2)
        self.assertIn((Vertex(3, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[5])
        self.assertIn((Vertex(6, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 1)
        self.assertIn((Vertex(2, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[6])

    def test_union_graph_union_kleene(self):
        self.g.new('a')
        self.g.union('b')
        graph = Graph()
        graph.new('c')
        graph.kleen_closure()
        self.g.union_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 8)

        self.assertEqual(len(self.g.adjlist[0]), 3)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), 'a'), self.g.adjlist[0])
        self.assertIn((Vertex(2, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[0])
        self.assertIn((Vertex(6, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((Vertex(3, Vertex.STATE_IN_PROCESS), 'b'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), ''), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 1)
        self.assertIn((Vertex(5, Vertex.STATE_IN_PROCESS), 'c'), self.g.adjlist[4])

        self.assertEqual(len(self.g.adjlist[5]), 2)
        self.assertIn((Vertex(4, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[5])
        self.assertIn((Vertex(7, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 2)
        self.assertIn((Vertex(4, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[6])
        self.assertIn((Vertex(7, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[6])

        self.assertEqual(len(self.g.adjlist[7]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), ''), self.g.adjlist[7])

    def test_union_graph(self):
        graph = Graph()
        self.g.union('a')
        self.g.union_graph(graph)
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        graph.new('b')
        self.g.union_graph(graph)
        self.assertEqual((self.g.start, self.g.finish), (0, 1))
        self.assertEqual(len(self.g.adjlist), 4)

        self.assertEqual(len(self.g.adjlist[0]), 2)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), 'a'), self.g.adjlist[0])
        self.assertIn((Vertex(2, Vertex.STATE_IN_PROCESS), ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((Vertex(3, Vertex.STATE_IN_PROCESS), 'b'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((Vertex(1, Vertex.STATE_FINISH), ''), self.g.adjlist[3])

