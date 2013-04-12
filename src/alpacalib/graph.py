"""
graph.py

Implement graph algorithm
"""

import copy

class InvalidGraphError(Exception):
    pass

class Graph:
    #
    #  adjlist
    #  +----+
    #  | [(v, e), (v, e), ...]
    #  +----+
    #  | [(v, e), (v, e), ...]
    #  +----+
    #  | []
    #  +----+
    #  | ...
    #  +----+
    #
    def __init__(self):
        self.adjlist = []
        self.start = -1
        self.finish = []

    def __iter__(self):
        for i in range(len(self.adjlist)):
            for v, e in self.adjlist[i]:
                if v != None:
                    yield i, v, e

    def new(self, edge):
        if len(self.adjlist) != 0:
            raise InvalidGraphError("Graph is non-empty.")

        self.adjlist.append([(1, edge)])
        self.adjlist.append([])
        self.start = 0
        self.finish.append(1)

    def new_graph(self, graph):
        if len(self.adjlist) != 0:
            raise InvalidGraphError("Graph is non-empyt.")

        if len(graph.adjlist) != 0:
            self.start = graph.start
            self.finish = copy.deepcopy(graph.finish)
            self.adjlist = copy.deepcopy(graph.adjlist)

    def new_relations(self, relations, start, finish):
        if start != 0 or len(finish) == 0:
            raise InvalidGraphError("Invalid start or finish.")

        self.start = start
        self.finish = copy.deepcopy(finish)
        self.adjlist = copy.deepcopy(relations)

    def concatenation(self, edge):
        if len(self.adjlist) == 0:
            self.new(edge)
        else:
            vcount = len(self.adjlist)
            self.adjlist.append([])
            self.adjlist[self.finish[-1]].append((vcount, edge))
            self.finish[-1] = vcount

    def concatenation_graph(self, graph):
        if len(self.adjlist) == 0:
            self.new_graph(graph)
        elif len(graph.adjlist) != 0:
            vcount = len(self.adjlist)
            self.adjlist.extend([[(v+vcount, e) for (v, e) in l] for l in graph.adjlist])
            self.adjlist[self.finish[-1]].append((graph.start+vcount, ''))
            self.finish[-1] = graph.finish[-1] + vcount

    def union(self, edge):
        if len(self.adjlist) == 0:
            self.new(edge)
        else:
            vcount = len(self.adjlist)
            self.adjlist.extend([[], []])
            self.adjlist[vcount].append((vcount+1, edge))
            self.adjlist[self.start].append((vcount, ''))
            self.adjlist[vcount+1].append((self.finish[-1], ''))

    def union_graph(self, graph):
        if len(self.adjlist) == 0:
            self.new_graph(graph)
        elif len(graph.adjlist) != 0:
            vcount = len(self.adjlist)
            self.adjlist.extend([[(v+vcount, e) for (v, e) in l] for l in graph.adjlist])
            self.adjlist[self.start].append((graph.start+vcount, ''))
            self.adjlist[graph.finish[-1]+vcount].append((self.finish[-1], ''))

    def kleene_closure(self):
        if len(self.adjlist) == 0:
            raise InvalidGraphError("Graph is empty.")

        vcount = len(self.adjlist)
        self.adjlist.extend([[], []])
        self.adjlist[self.finish[-1]].extend([(self.start, ''), (vcount+1, '')])
        self.adjlist[vcount].extend([(self.start, ''), (vcount+1, '')])
        self.start = vcount
        self.finish[-1] = vcount + 1

    def get_peer_vertices(self, vertex, edge):
        if vertex >= len(self.adjlist):
            raise InvalidGraphError("Invalid vertex.")

        return {v for v, e in self.adjlist[vertex] if e == edge}

    def unique(self, vset):
        if len(vset) > 1:
            base_v = None
            if self.start in vset:
                base_v = self.start
            else:
                l = list(vset)
                l.sort()
                base_v = l[0]

            for vertex in range(len(self.adjlist)):
                if vertex != base_v and vertex in vset:
                    self.adjlist[vertex][:] = []
                    self.adjlist[vertex].append((None, None))
                    if vertex in self.finish:
                        self.finish.remove(vertex)
                else:
                    for v, e in self.adjlist[vertex]:
                        if v in vset:
                            index = self.adjlist[vertex].index((v, e))
                            self.adjlist[vertex][index] = (base_v, e)

