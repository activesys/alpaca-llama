"""
test_rast.py
unittesting for RAST
"""

import unittest
from alpaca.rast import RAST
from alpaca.graph import Graph
from alpaca.syntax import SyntaxParser
from alpaca.charset import CharacterSet

class TestRAST(unittest.TestCase):
    def test_is_empty(self):
        self.rast = RAST()
        self.assertTrue(self.rast.is_empty())

        self.syntax = SyntaxParser('a')
        self.rast = self.syntax.build()
        self.assertFalse(self.rast.is_empty())

    def test_traversal_operand(self):
        self.rast = SyntaxParser('a').build()
        self.g = Graph()
        self.g.new('a')
        g = self.rast.traversal()
        self.assertEqual((g.start, g.finish, g.adjlist), (self.g.start, self.g.finish, self.g.adjlist))

    def test_traversal_concatenation(self):
        self.rast = SyntaxParser('ab').build()
        self.g = Graph()
        self.g.new('a')
        graph = Graph()
        graph.new('b')
        self.g.concatenation_graph(graph)
        g = self.rast.traversal()
        self.assertEqual((g.start, g.finish, g.adjlist), (self.g.start, self.g.finish, self.g.adjlist))

    def test_traversal_union(self):
        self.rast = SyntaxParser('a|b').build()
        self.g = Graph()
        self.g.new('a')
        graph = Graph()
        graph.new('b')
        self.g.union_graph(graph)
        g = self.rast.traversal()
        self.assertEqual((g.start, g.finish, g.adjlist), (self.g.start, self.g.finish, self.g.adjlist))

    def test_traversal_kleene_closure(self):
        self.rast = SyntaxParser('a*').build()
        self.g = Graph()
        self.g.new('a')
        self.g.kleene_closure()
        g = self.rast.traversal()
        self.assertEqual((g.start, g.finish, g.adjlist), (self.g.start, self.g.finish, self.g.adjlist))

    def test_traversal_positive_closure(self):
        self.rast = SyntaxParser('a+').build()
        self.g = Graph()
        self.g.new('a')
        tmp = Graph()
        tmp.new('a')
        tmp.kleene_closure()
        self.g.concatenation_graph(tmp)
        g = self.rast.traversal()
        self.assertEqual((g.start, g.finish, g.adjlist), (self.g.start, self.g.finish, self.g.adjlist))

    def test_traversal_pset(self):
        self.rast = SyntaxParser('[a]').build()
        self.g = Graph()
        cset = CharacterSet.intersection_set('a')
        for char in cset:
            self.g.union(char)
        g = self.rast.traversal()
        self.assertEqual((g.start, g.finish, g.adjlist), (self.g.start, self.g.finish, self.g.adjlist))

    def test_traversal_pset_range(self):
        self.rast = SyntaxParser('[a-z]').build()
        self.g = Graph()
        cset = CharacterSet.intersection_set('a', 'z')
        for char in cset:
            self.g.union(char)
        g = self.rast.traversal()
        self.assertEqual((g.start, g.finish, g.adjlist), (self.g.start, self.g.finish, self.g.adjlist))

    def test_traversal_nset(self):
        self.rast = SyntaxParser('[^a]').build()
        self.g = Graph()
        cset = CharacterSet.complementary_set('a')
        for char in cset:
            self.g.union(char)
        g = self.rast.traversal()
        self.assertEqual((g.start, g.finish, g.adjlist), (self.g.start, self.g.finish, self.g.adjlist))

    def test_traversal_pset_range(self):
        self.rast = SyntaxParser('[^a-z]').build()
        self.g = Graph()
        cset = CharacterSet.complementary_set('a', 'z')
        for char in cset:
            self.g.union(char)
        g = self.rast.traversal()
        self.assertEqual((g.start, g.finish, g.adjlist), (self.g.start, self.g.finish, self.g.adjlist))

