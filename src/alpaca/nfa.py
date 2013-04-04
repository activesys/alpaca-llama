"""
nfa.py
Implementation of NFA
"""

from graph import Graph

class NFA:
    def __init__(self, graph=None):
        self.graph = graph

    def merge(self, nfas):
        if len(nfas) == 0:
            return
        else:
            if self.graph == None:
                self.graph = Graph()
            for nfa in nfas:
                self.graph.union_graph(nfa.graph)

    def __move(self, vertices, edge):
        new_vertices = set()
        for vertex in vertices:
            new_vertices.update(self.graph.get_peer_vertices(vertex, edge))
        return new_vertices

    def __epsilon_closure(self, vertices):
        eset = set()
        while True:
            tmp_set = set()
            for vertex in vertices.difference(eset):
                tmp_set.update(self.graph.get_peer_vertices(vertex, ''))
            eset.update(vertices)
            vertices = tmp_set
            if len(vertices) == 0:
                break
        return eset

