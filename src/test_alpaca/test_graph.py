"""
test_graph.py

unittesting for graph.
"""

import unittest
from alpacalib.graph import Graph
from alpacalib.graph import InvalidGraphError
from alpacalib.setrelation import SetRelation

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g = Graph()

    def test_new(self):
        self.g.new('a')
        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertRaises(InvalidGraphError, self.g.new, 'b')

    def test_concatenation(self):
        self.g.concatenation('a')
        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.g.concatenation('b')
        self.assertEqual((self.g.start, self.g.finish), (0, [2]))
        self.assertEqual(len(self.g.adjlist), 3)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((2, 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 0)

    def test_union(self):
        self.g.union('a')
        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.g.union('b')
        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 4)

        self.assertEqual(len(self.g.adjlist[0]), 2)
        self.assertIn((1, 'a'), self.g.adjlist[0])
        self.assertIn((2, ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((3, 'b'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((1, ''), self.g.adjlist[3])

    def test_kleene_closure(self):
        self.assertRaises(InvalidGraphError, self.g.kleene_closure)

        self.g.new('a')
        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.g.kleene_closure()
        self.assertEqual((self.g.start, self.g.finish), (2, [3]))
        self.assertEqual(len(self.g.adjlist), 4)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 2)
        self.assertIn((0, ''), self.g.adjlist[1])
        self.assertIn((3, ''), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 2)
        self.assertIn((0, ''), self.g.adjlist[2])
        self.assertIn((3, ''), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 0)

    def test_new_graph(self):
        graph = Graph()

        graph.new('a')
        self.g.new_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertRaises(InvalidGraphError, self.g.new_graph, graph)

    def test_concatenation_graph(self):
        graph = Graph()
        self.g.new('a')
        self.g.concatenation_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        graph.new('b')
        self.g.concatenation_graph(graph)
        self.assertEqual((self.g.start, self.g.finish), (0, [3]))
        self.assertEqual(len(self.g.adjlist), 4)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((2, ''), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((3, 'b'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 0)

    def test_concatenation_graph_empty(self):
        graph = Graph()
        graph.new('a')
        self.g.concatenation_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

    def test_concatenation_graph_union_kleene(self):
        self.g.new('a')
        self.g.union('b')
        graph = Graph()
        graph.new('c')
        graph.kleene_closure()
        self.g.concatenation_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, [7]))
        self.assertEqual(len(self.g.adjlist), 8)

        self.assertEqual(len(self.g.adjlist[0]), 2)
        self.assertIn((1, 'a'), self.g.adjlist[0])
        self.assertIn((2, ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((6, ''), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((3, 'b'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((1, ''), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 1)
        self.assertIn((5, 'c'), self.g.adjlist[4])

        self.assertEqual(len(self.g.adjlist[5]), 2)
        self.assertIn((4, ''), self.g.adjlist[5])
        self.assertIn((7, ''), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 2)
        self.assertIn((4, ''), self.g.adjlist[6])
        self.assertIn((7, ''), self.g.adjlist[6])

        self.assertEqual(len(self.g.adjlist[7]), 0)

    def test_concatenation_graph_concatenation_kleene(self):
        self.g.new('a')
        self.g.concatenation('b')
        graph = Graph()
        graph.new('c')
        graph.kleene_closure()
        self.g.concatenation_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, [6]))
        self.assertEqual(len(self.g.adjlist), 7)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((2, 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((5, ''), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((4, 'c'), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 2)
        self.assertIn((3, ''), self.g.adjlist[4])
        self.assertIn((6, ''), self.g.adjlist[4])

        self.assertEqual(len(self.g.adjlist[5]), 2)
        self.assertIn((3, ''), self.g.adjlist[5])
        self.assertIn((6, ''), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 0)

    def test_concatenation_graph_concatenation_union(self):
        self.g.new('a')
        self.g.concatenation('b')
        graph = Graph()
        graph.new('c')
        graph.union('d')
        self.g.concatenation_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, [4]))
        self.assertEqual(len(self.g.adjlist), 7)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((2, 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((3, ''), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 2)
        self.assertIn((4, 'c'), self.g.adjlist[3])
        self.assertIn((5, ''), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 0)

        self.assertEqual(len(self.g.adjlist[5]), 1)
        self.assertIn((6, 'd'), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 1)
        self.assertIn((4, ''), self.g.adjlist[6])

    def test_union_graph_union_concatenation(self):
        self.g.new('a')
        self.g.union('b')
        graph = Graph()
        graph.new('c')
        graph.concatenation('d')
        self.g.union_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 7)

        self.assertEqual(len(self.g.adjlist[0]), 3)
        self.assertIn((1, 'a'), self.g.adjlist[0])
        self.assertIn((2, ''), self.g.adjlist[0])
        self.assertIn((4, ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((3, 'b'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((1, ''), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 1)
        self.assertIn((5, 'c'), self.g.adjlist[4])

        self.assertEqual(len(self.g.adjlist[5]), 1)
        self.assertIn((6, 'd'), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 1)
        self.assertIn((1, ''), self.g.adjlist[6])

    def test_union_graph_concatenation_kleene(self):
        self.g.new('a')
        self.g.concatenation('b')
        graph = Graph()
        graph.new('c')
        graph.kleene_closure()
        self.g.union_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, [2]))
        self.assertEqual(len(self.g.adjlist), 7)

        self.assertEqual(len(self.g.adjlist[0]), 2)
        self.assertIn((1, 'a'), self.g.adjlist[0])
        self.assertIn((5, ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 1)
        self.assertIn((2, 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 0)

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((4, 'c'), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 2)
        self.assertIn((3, ''), self.g.adjlist[4])
        self.assertIn((6, ''), self.g.adjlist[4])

        self.assertEqual(len(self.g.adjlist[5]), 2)
        self.assertIn((3, ''), self.g.adjlist[5])
        self.assertIn((6, ''), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 1)
        self.assertIn((2, ''), self.g.adjlist[6])

    def test_union_graph_union_kleene(self):
        self.g.new('a')
        self.g.union('b')
        graph = Graph()
        graph.new('c')
        graph.kleene_closure()
        self.g.union_graph(graph)

        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 8)

        self.assertEqual(len(self.g.adjlist[0]), 3)
        self.assertIn((1, 'a'), self.g.adjlist[0])
        self.assertIn((2, ''), self.g.adjlist[0])
        self.assertIn((6, ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((3, 'b'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((1, ''), self.g.adjlist[3])

        self.assertEqual(len(self.g.adjlist[4]), 1)
        self.assertIn((5, 'c'), self.g.adjlist[4])

        self.assertEqual(len(self.g.adjlist[5]), 2)
        self.assertIn((4, ''), self.g.adjlist[5])
        self.assertIn((7, ''), self.g.adjlist[5])

        self.assertEqual(len(self.g.adjlist[6]), 2)
        self.assertIn((4, ''), self.g.adjlist[6])
        self.assertIn((7, ''), self.g.adjlist[6])

        self.assertEqual(len(self.g.adjlist[7]), 1)
        self.assertIn((1, ''), self.g.adjlist[7])

    def test_union_graph_empty(self):
        graph = Graph()
        graph.new('a')
        self.g.union_graph(graph)
        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

    def test_union_graph(self):
        graph = Graph()
        self.g.union('a')
        self.g.union_graph(graph)
        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 2)

        self.assertEqual(len(self.g.adjlist[0]), 1)
        self.assertIn((1, 'a'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        graph.new('b')
        self.g.union_graph(graph)
        self.assertEqual((self.g.start, self.g.finish), (0, [1]))
        self.assertEqual(len(self.g.adjlist), 4)

        self.assertEqual(len(self.g.adjlist[0]), 2)
        self.assertIn((1, 'a'), self.g.adjlist[0])
        self.assertIn((2, ''), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 0)

        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((3, 'b'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 1)
        self.assertIn((1, ''), self.g.adjlist[3])

    def test_get_peer_vertices_invalid_vertiex(self):
        self.g.new('a')
        self.g.kleene_closure()
        self.g.union('b')
        self.assertRaises(InvalidGraphError, self.g.get_peer_vertices, 9, 'a')
    def test_get_peer_vertices_invalid_edge(self):
        self.g.new('a')
        self.g.kleene_closure()
        self.g.union('b')
        self.assertEqual(self.g.get_peer_vertices(2, 'c'), set())
    def test_get_peer_vertices_a(self):
        self.g.new('a')
        self.g.kleene_closure()
        self.g.union('b')
        self.assertEqual(self.g.get_peer_vertices(0, 'a'), {1})
    def test_get_peer_vertices_epsilon(self):
        self.g.new('a')
        self.g.kleene_closure()
        self.g.union('b')
        self.assertEqual(self.g.get_peer_vertices(2, ''), {0, 3, 4})

    def test_new_relations(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.add_relation({1, 2, 3}, {4, 5}, 'a')
        self.relation.add_relation({1, 2, 3}, {7, 8, 9}, 'b')
        self.relation.add_relation({1, 2, 3}, {6}, 'c')
        self.relation.add_relation({4, 5}, {4, 5}, 'a')
        self.relation.add_relation({4, 5}, {7, 8, 9}, 'b')
        self.relation.add_relation({7, 8, 9}, {1, 2, 3}, 'e')
        self.relation.add_relation({7, 8, 9}, {6}, 'f')
        self.relation.set_finish([4, 6])
        self.g.new_relations(self.relation.get_relations(), self.relation.start, self.relation.finish)

        self.assertEqual((self.g.start, self.g.finish), (0, [1, 3]))
        self.assertEqual(len(self.g.adjlist), 4)

        self.assertEqual(len(self.g.adjlist[0]), 3)
        self.assertIn((1, 'a'), self.g.adjlist[0])
        self.assertIn((2, 'b'), self.g.adjlist[0])
        self.assertIn((3, 'c'), self.g.adjlist[0])

        self.assertEqual(len(self.g.adjlist[1]), 2)
        self.assertIn((1, 'a'), self.g.adjlist[1])
        self.assertIn((2, 'b'), self.g.adjlist[1])

        self.assertEqual(len(self.g.adjlist[2]), 2)
        self.assertIn((0, 'e'), self.g.adjlist[2])
        self.assertIn((3, 'f'), self.g.adjlist[2])

        self.assertEqual(len(self.g.adjlist[3]), 0)

    def test_new_relations_error_start(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.add_relation({1, 2, 3}, {4, 5}, 'a')
        self.relation.add_relation({1, 2, 3}, {7, 8, 9}, 'b')
        self.relation.add_relation({1, 2, 3}, {6}, 'c')
        self.relation.add_relation({4, 5}, {4, 5}, 'a')
        self.relation.add_relation({4, 5}, {7, 8, 9}, 'b')
        self.relation.add_relation({7, 8, 9}, {1, 2, 3}, 'e')
        self.relation.add_relation({7, 8, 9}, {6}, 'f')
        self.relation.set_finish([4, 6])
        self.assertRaises(
            InvalidGraphError, self.g.new_relations,
            self.relation.get_relations(), 2, self.relation.finish)
    def test_new_relations_error_finish(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.add_relation({1, 2, 3}, {4, 5}, 'a')
        self.relation.add_relation({1, 2, 3}, {7, 8, 9}, 'b')
        self.relation.add_relation({1, 2, 3}, {6}, 'c')
        self.relation.add_relation({4, 5}, {4, 5}, 'a')
        self.relation.add_relation({4, 5}, {7, 8, 9}, 'b')
        self.relation.add_relation({7, 8, 9}, {1, 2, 3}, 'e')
        self.relation.add_relation({7, 8, 9}, {6}, 'f')
        self.relation.set_finish([4, 6])
        self.assertRaises(
            InvalidGraphError, self.g.new_relations,
            self.relation.get_relations(), self.relation.start, [])

    def test_unique_none_equal(self):
        self.g.adjlist.extend([[(1, 'a'), (2, 'b'), (3, 'c')], [(1, 'a'), (3, 'c')], [(2, 'b'), (3, 'c')], []])
        self.g.start = 0
        self.g.finish = [3]
        self.g.unique({1})
        self.assertEqual(len(self.g.adjlist), 4)
        self.assertEqual((self.g.start, self.g.finish), (0, [3]))
        self.assertEqual(len(self.g.adjlist[0]), 3)
        self.assertIn((1, 'a'), self.g.adjlist[0])
        self.assertIn((2, 'b'), self.g.adjlist[0])
        self.assertIn((3, 'c'), self.g.adjlist[0])
        self.assertEqual(len(self.g.adjlist[1]), 2)
        self.assertIn((1, 'a'), self.g.adjlist[1])
        self.assertIn((3, 'c'), self.g.adjlist[1])
        self.assertEqual(len(self.g.adjlist[2]), 2)
        self.assertIn((2, 'b'), self.g.adjlist[2])
        self.assertIn((3, 'c'), self.g.adjlist[2])
        self.assertEqual(len(self.g.adjlist[3]), 0)
    def test_unique(self):
        self.g.adjlist.extend(
            [[(1,'a'),(2,'b'),(4,'d')],[(1,'a'),(3,'c')],[(1,'a'),(2,'b'),(4,'d')],
             [(3,'c'),(4,'d'),(5,'e')],[(3,'c'),(4,'d'),(5,'e')],[]])
        self.g.start = 0
        self.g.finish = [3, 4, 5]
        self.g.unique({0, 2})
        self.assertEqual(len(self.g.adjlist), 6)
        self.assertEqual((self.g.start, self.g.finish), (0, [3, 4, 5]))
        self.assertEqual(len(self.g.adjlist[0]), 3)
        self.assertIn((1, 'a'), self.g.adjlist[0])
        self.assertIn((0, 'b'), self.g.adjlist[0])
        self.assertIn((4, 'd'), self.g.adjlist[0])
        self.assertEqual(len(self.g.adjlist[1]), 2)
        self.assertIn((1, 'a'), self.g.adjlist[1])
        self.assertIn((3, 'c'), self.g.adjlist[1])
        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((None, None), self.g.adjlist[2])
        self.assertEqual(len(self.g.adjlist[3]), 3)
        self.assertIn((3, 'c'), self.g.adjlist[3])
        self.assertIn((4, 'd'), self.g.adjlist[3])
        self.assertIn((5, 'e'), self.g.adjlist[3])
        self.assertEqual(len(self.g.adjlist[4]), 3)
        self.assertIn((3, 'c'), self.g.adjlist[4])
        self.assertIn((4, 'd'), self.g.adjlist[4])
        self.assertIn((5, 'e'), self.g.adjlist[4])
        self.assertEqual(len(self.g.adjlist[5]), 0)
        self.g.unique({3, 4})
        self.assertEqual(len(self.g.adjlist), 6)
        self.assertEqual((self.g.start, self.g.finish), (0, [3, 5]))
        self.assertEqual(len(self.g.adjlist[0]), 3)
        self.assertIn((1, 'a'), self.g.adjlist[0])
        self.assertIn((0, 'b'), self.g.adjlist[0])
        self.assertIn((3, 'd'), self.g.adjlist[0])
        self.assertEqual(len(self.g.adjlist[1]), 2)
        self.assertIn((1, 'a'), self.g.adjlist[1])
        self.assertIn((3, 'c'), self.g.adjlist[1])
        self.assertEqual(len(self.g.adjlist[2]), 1)
        self.assertIn((None, None), self.g.adjlist[2])
        self.assertEqual(len(self.g.adjlist[3]), 3)
        self.assertIn((3, 'c'), self.g.adjlist[3])
        self.assertIn((3, 'd'), self.g.adjlist[3])
        self.assertIn((5, 'e'), self.g.adjlist[3])
        self.assertEqual(len(self.g.adjlist[4]), 1)
        self.assertIn((None, None), self.g.adjlist[4])
        self.assertEqual(len(self.g.adjlist[5]), 0)

    def test_inter(self):
        self.g.adjlist.extend(
            [[(1,'a'),(0,'b'),(3,'d')],[(1,'a'),(3,'c')],[(None, None)],
             [(3,'c'),(3,'d'),(5,'e')],[(None, None)],[]])
        self.g.start = 0
        self.g.finish = [3, 5]
        i = iter(self.g)
        self.assertEqual(next(i), (0, 1, 'a'))
        self.assertEqual(next(i), (0, 0, 'b'))
        self.assertEqual(next(i), (0, 3, 'd'))
        self.assertEqual(next(i), (1, 1, 'a'))
        self.assertEqual(next(i), (1, 3, 'c'))
        self.assertEqual(next(i), (3, 3, 'c'))
        self.assertEqual(next(i), (3, 3, 'd'))
        self.assertEqual(next(i), (3, 5, 'e'))
        self.assertRaises(StopIteration, next, i)

