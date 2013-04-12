"""
nfa.py
Implementation of NFA
"""

from alpacalib.graph import Graph
from alpacalib.charset import CharacterSet
from alpacalib.setrelation import SetRelation
from alpacalib.dfa import DFA

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


    def transform(self):
        eset = self.__epsilon_closure({self.graph.start})
        relation = SetRelation(eset)
        while not relation.is_all_marked():
            unmarked_set = relation.get_non_marked()
            relation.mark(unmarked_set)
            for c in CharacterSet.cset:
                cset = self.__move(unmarked_set, c)
                eset = self.__epsilon_closure(cset)
                if len(eset) > 0:
                    relation.add_relation(unmarked_set, eset, c)
            for c in CharacterSet.operator:
                cset = self.__move(unmarked_set, c)
                eset = self.__epsilon_closure(cset)
                if len(eset) > 0:
                    relation.add_relation(unmarked_set, eset, c)
        relation.set_finish(self.graph.finish)

        rs = relation.get_relations()
        graph = Graph()
        graph.new_relations(rs, relation.start, relation.finish)
        return DFA(graph)


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


