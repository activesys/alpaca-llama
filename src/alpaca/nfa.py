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

