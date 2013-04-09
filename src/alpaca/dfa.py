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

        for aset in old_sets:
            self.graph.unique(aset)

        #relation = None
        #start_set = None
        #for aset in old_sets:
            #if self.graph.start in aset:
                #relation = SetRelation(aset)
                #start_set = aset
                #break

        ## depth-first search
        #for aset in old_sets:
            #rl = self.graph.adjlist[list(aset)[0]]
            #for v, e in rl:
                #if v in aset:
                    #relation.add_relation(aset, aset, e)
                #else:
                    #relation.add_relation(aset, {v}, e)
        #relation.set_finish(self.graph.finish)

        #graph = Graph()
        #graph.new_relations(relation.get_relations(), relation.start, relation.finish)
        #self.graph = graph


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


