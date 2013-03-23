"""
test_lex.py

unit testing for lex.py
"""

import unittest
from lex import LexParser
from lex import EndOfRegex

class TestLexParser(unittest.TestCase):
    def test_get_token_letter(self):
        self.lex = LexParser('a')
        self.assertEqual(self.lex.get_token(), 'a')

    def test_get_token_number(self):
        self.lex = LexParser('9')
        self.assertEqual(self.lex.get_token(), '9')

    def test_get_token_char(self):
        self.lex = LexParser('$')
        self.assertEqual(self.lex.get_token(), '$')

    def test_get_token_operator(self):
        self.lex = LexParser('*')
        self.assertEqual(self.lex.get_token(), '*')

    def test_get_token_escape(self):
        self.lex = LexParser('\\(')
        self.assertEqual(self.lex.get_token(), '\\(')

    def test_get_token_abbreviation(self):
        self.lex = LexParser('\\t')
        self.assertEqual(self.lex.get_token(), '\\t')

    def test_get_token_mnemonic(self):
        self.lex = LexParser('\\w')
        self.assertEqual(self.lex.get_token(), '\\w')

    def test_get_token_backslash(self):
        self.lex = LexParser('\\')
        self.assertEqual(self.lex.get_token(), '\\')

    def test_get_token_eor(self):
        self.lex = LexParser('')
        self.assertRaises(EndOfRegex, self.lex.get_token)

    def test_get_token_all(self):
        self.lex = LexParser('(\\l%=\\f)|\\**\\')
        self.assertEqual(self.lex.get_token(), '(')
        self.assertEqual(self.lex.get_token(), '\\l')
        self.assertEqual(self.lex.get_token(), '%')
        self.assertEqual(self.lex.get_token(), '=')
        self.assertEqual(self.lex.get_token(), '\\f')
        self.assertEqual(self.lex.get_token(), ')')
        self.assertEqual(self.lex.get_token(), '|')
        self.assertEqual(self.lex.get_token(), '\\*')
        self.assertEqual(self.lex.get_token(), '*')
        self.assertEqual(self.lex.get_token(), '\\')
        self.assertRaises(EndOfRegex, self.lex.get_token)

