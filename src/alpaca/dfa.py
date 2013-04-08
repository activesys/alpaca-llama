"""
dfa.py
Implementation for DFA
"""

from graph import Graph
from setrelation import SetRelation
from charset import CharacterSet

class DFA:
    def __init__(self, graph=None):
        self.graph = graph

    def minimize(self):
        finish_set = set(self.graph.finish)
        nonfinish_set = {s for s in range(len(self.graph.adjlist))}
        nonfinish_set.difference_update(finish_set)
        old_sets = {nonfinish_set, finish_set}

        relation = None
        for c in CharacterSet.cset:
            new_sets = self.__split(old_sets, c)
            old_sets = new_sets

        # new relation from split and graph
        relation = SetRelation()
        # some code.
        graph = Graph()
        graph.new_relations(relation.get_relations(), relation.start, relation.finish)
        self.graph = graph

    def __split(self, old_sets, c):
        relation_dict = {}
        new_sets = set()
        for aset in old_sets:
            for src_state in aset:
                dst_state = self.graph.get_vertex(src_state, c)
                if dst_state in relation_dict:
                    relation_dict[{dst_state}].add(src_state)
                else:
                    relation_dict[{dst_state}] = {src_state}
            new_sets.update(relation_dict.values())

        return new_sets

