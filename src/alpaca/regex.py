"""
regex.py
Implementation for Regex.
"""

from syntax import SyntaxParser
from syntax import SyntaxParserError
from rast import RAST
from graph import Graph
from nfa import NFA

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

