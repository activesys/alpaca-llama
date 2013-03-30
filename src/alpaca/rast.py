"""
rast.py

Regex Abstract Syntax Tree
"""

from graph import Graph
from charset import CharacterSet

class RASTError(Exception):
    pass

# Regex: [^a-zA-Z]*[abc-f]+$&|@!
#                                    '|'
#                              /           \
#                             ''           ''
#            /              /   \   \     /  \
#           '*'            '+'  'h' 'i'  '@' '!'
#            |             |
#          '[^]'          '[]'
#        /      \       /   |   \
#      '-'     '-'     'a' 'b'   '-'
#     /   \    /  \             /   \
#    'a'  'z' 'A' 'Z'         'c'   'f'

class RAST:
    def __init__(self):
        self.is_operator = False
        self.token = ''
        self.children = []

    def is_empty(self):
        return not self.is_operator and self.token == '' and len(self.children) == 0

    def traversal(self):
        graph = Graph()
        if not self.is_operator:
            graph.new(self.token)
            return graph
        elif self.token == '':
            for child in self.children:
                graph.concatenation_graph(child.traversal())
            return graph
        elif self.token == '|':
            for child in self.children:
                graph.union_graph(child.traversal())
            return graph
        elif self.token == '*':
            graph.new_graph(self.children[0].traversal())
            graph.kleen_closure()
            return graph
        elif self.token == '+':
            graph.new_graph(self.children[0].traversal())
            g = Graph()
            g.new_graph(graph)
            g.kleen_closure()
            graph.concatenation_graph(g)
            return graph
        elif self.token == '[]':
            clist = []
            for child in self.children:
                if not child.is_operator:
                    clist.append(child.token)
                else:
                    clist += CharacterSet.intersection_set(child.children[0].token, child.children[1].token)
            for char in clist:
                graph.union(char)
            return graph
        elif self.token == '[^]':
            clist = []
            for child in self.children:
                if not child.is_operator:
                    clist.append(child.token)
                else:
                    clist += CharacterSet.intersection_set(child.children[0].token, child.children[1].token)
            for char in CharacterSet.complementary_set_full(clist):
                graph.union(char)
            return graph
        else:
            raise RASTError

