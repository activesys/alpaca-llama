"""
regex.py
Implementation for Regex.
"""

from alpacalib.syntax import SyntaxParser
from alpacalib.syntax import SyntaxParserError
from alpacalib.rast import RAST
from alpacalib.graph import Graph
from alpacalib.nfa import NFA

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

