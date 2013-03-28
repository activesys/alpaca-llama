"""
graph.py

Implement graph algorithm
"""

class GraphNonEmptyError(Exception):
    pass

class Vertex:
    STATE_START = 'START'
    STATE_IN_PROCESS = 'IN-PROCESS'
    STATE_FINISH = 'FINISH'

    def __init__(self, index, state):
        self.index = index
        self.state = state

class Graph:
    def __init__(self):
        self.adjlist = []
        self.start = -1
        self.finish = -1

    def new(self, edge):
        if len(self.adjlist) != 0:
            raise GraphNonEmptyError("Graph is non-empty.")

        

