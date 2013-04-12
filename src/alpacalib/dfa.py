"""
dfa.py
Implementation for DFA
"""

from alpacalib.graph import Graph
from alpacalib.setrelation import SetRelation
from alpacalib.charset import CharacterSet
from alpacalib.dot import Dot

class DFA:
    def __init__(self, graph=None):
        self.graph = graph


    def minimize(self):
        finish_set = set(self.graph.finish)
        nonfinish_set = {s for s in range(len(self.graph.adjlist))}
        nonfinish_set.difference_update(finish_set)
        old_sets = [nonfinish_set, finish_set]

        relation = None
        for c in CharacterSet.cset:
            for aset in old_sets:
                if len(aset) > 1:
                    break
            else:
                break
            new_sets = self.__split(old_sets, c)
            old_sets = new_sets
        for c in CharacterSet.operator:
            for aset in old_sets:
                if len(aset) > 1:
                    break
            else:
                break
            new_sets = self.__split(old_sets, c)
            old_sets = new_sets

        for aset in old_sets:
            self.graph.unique(aset)

    def transform(self):
        dot = Dot()
        dot.start(self.graph.start, self.graph.finish)
        for vb, ve, e in self.graph:
            dot.new_edge(vb, ve, e)
        dot.end()
        return dot


    def __split(self, old_sets, c):
        if len(old_sets) <= 1:
            return old_sets

        new_sets = []
        for aset in old_sets:
            relation_dict = {}
            for src_state in aset:
                dst_set = self.graph.get_peer_vertices(src_state, c)
                if frozenset(dst_set) in relation_dict:
                    relation_dict[frozenset(dst_set)].add(src_state)
                else:
                    relation_dict[frozenset(dst_set)] = {src_state}
            new_sets.extend(relation_dict.values())

        return new_sets


