"""
regex.py
Implementation for Regex.
"""

from syntax import SyntaxParser
from rast import RAST
from graph import Graph
from nfa import NFA

class Regex:
    def __init__(self, text):
        self.rast = SyntaxParser(text).build()

    def transform(self):
        return NFA(self.rast.traversal())

