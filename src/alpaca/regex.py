"""
regex.py
Implementation for Regex.
"""

from alpaca.syntax import SyntaxParser
from alpaca.syntax import SyntaxParserError
from alpaca.rast import RAST
from alpaca.graph import Graph
from alpaca.nfa import NFA

class RegexError(Exception):
    pass

class Regex:
    def __init__(self, text):
        try:
            self.rast = SyntaxParser(text).build()
        except SyntaxParserError as err:
            raise RegexError(err.args[0])

    def transform(self):
        return NFA(self.rast.traversal())

