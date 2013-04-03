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
        vs = []
        for vertex in vertices:
            vs.extend(self.graph.get_peer_vertices(vertex, edge))
        vs = list(set(vs))
        vs.sort()
        return vs

