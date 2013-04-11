"""
test_lex.py

unit testing for lex.py
"""

import unittest
from lex import LexParser
from lex import TokenStrategy

class TestTokenStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = TokenStrategy()

    def test_is_operator_number(self):
        self.assertFalse(self.strategy.is_operator('5'))
        self.assertFalse(self.strategy.is_operator('4', inset=True))
        self.assertFalse(self.strategy.is_operator('2', inset=True, firstchar=True))

    def test_is_operator_letter(self):
        self.assertFalse(self.strategy.is_operator('a'))
        self.assertFalse(self.strategy.is_operator('a', inset=True))
        self.assertFalse(self.strategy.is_operator('a', inset=True, firstchar=True))

    def test_is_operator_char(self):
        self.assertFalse(self.strategy.is_operator('&'))
        self.assertFalse(self.strategy.is_operator('$', inset=True))
        self.assertFalse(self.strategy.is_operator('#', inset=True, firstchar=True))

    def test_is_operator_escape(self):
        self.assertFalse(self.strategy.is_operator('\\|'))
        self.assertFalse(self.strategy.is_operator('\\*', inset=True))
        self.assertFalse(self.strategy.is_operator('\\\\', inset=True, firstchar=True))

    def test_is_operator_abbreviation(self):
        self.assertFalse(self.strategy.is_operator('\\a'))
        self.assertFalse(self.strategy.is_operator('\\b', inset=True))
        self.assertFalse(self.strategy.is_operator('\\c', inset=True, firstchar=True))

    def test_is_operator_mnemonic(self):
        self.assertFalse(self.strategy.is_operator('\\d'))
        self.assertFalse(self.strategy.is_operator('\\D', inset=True))
        self.assertFalse(self.strategy.is_operator('\\W', inset=True, firstchar=True))

    def test_is_operator_union(self):
        self.assertTrue(self.strategy.is_operator('|'))
        self.assertFalse(self.strategy.is_operator('|', inset=True))
        self.assertFalse(self.strategy.is_operator('|', inset=True, firstchar=True))

    def test_is_operator_kleene_closure(self):
        self.assertTrue(self.strategy.is_operator('*'))
        self.assertFalse(self.strategy.is_operator('*', inset=True))
        self.assertFalse(self.strategy.is_operator('*', inset=True, firstchar=True))

    def test_is_operator_positive_closure(self):
        self.assertTrue(self.strategy.is_operator('+'))
        self.assertFalse(self.strategy.is_operator('+', inset=True))
        self.assertFalse(self.strategy.is_operator('+', inset=True, firstchar=True))

    def test_is_operator_left_parenthesis(self):
        self.assertTrue(self.strategy.is_operator('('))
        self.assertFalse(self.strategy.is_operator('(', inset=True))
        self.assertFalse(self.strategy.is_operator('(', inset=True, firstchar=True))

    def test_is_operator_right_parenthesis(self):
        self.assertTrue(self.strategy.is_operator(')'))
        self.assertFalse(self.strategy.is_operator(')', inset=True))
        self.assertFalse(self.strategy.is_operator(')', inset=True, firstchar=True))

    def test_is_operator_backslash(self):
        self.assertTrue(self.strategy.is_operator('\\'))
        self.assertTrue(self.strategy.is_operator('\\', inset=True))
        self.assertTrue(self.strategy.is_operator('\\', inset=True, firstchar=True))

    def test_is_operator_pointer(self):
        self.assertTrue(self.strategy.is_operator('.'))
        self.assertFalse(self.strategy.is_operator('.', inset=True))
        self.assertFalse(self.strategy.is_operator('.', inset=True, firstchar=True))

    def test_is_operator_caret(self):
        self.assertFalse(self.strategy.is_operator('^'))
        self.assertFalse(self.strategy.is_operator('^', inset=True))
        self.assertTrue(self.strategy.is_operator('^', inset=True, firstchar=True))

    def test_is_operator_left_brackets(self):
        self.assertTrue(self.strategy.is_operator('['))
        self.assertTrue(self.strategy.is_operator('[', inset=True))
        self.assertTrue(self.strategy.is_operator('[', inset=True, firstchar=True))

    def test_is_operator_right_brackets(self):
        self.assertTrue(self.strategy.is_operator(']'))
        self.assertTrue(self.strategy.is_operator(']', inset=True))
        self.assertTrue(self.strategy.is_operator(']', inset=True, firstchar=True))

    def test_is_operator_range(self):
        self.assertFalse(self.strategy.is_operator('-'))
        self.assertTrue(self.strategy.is_operator('-', inset=True))
        self.assertTrue(self.strategy.is_operator('-', inset=True, firstchar=True))


class TestLexParser(unittest.TestCase):
    def test_get_token_letter(self):
        self.lex = LexParser('a')
        self.assertEqual(self.lex.get_token(), (False, 'a'))
    def test_get_token_letter_inset(self):
        self.lex = LexParser('a')
        self.assertEqual(self.lex.get_token(inset=True), (False, 'a'))
    def test_get_token_letter_firstchar(self):
        self.lex = LexParser('a')
        self.assertEqual(self.lex.get_token(inset=True, firstchar=True), (False, 'a'))

    def test_get_token_number(self):
        self.lex = LexParser('9')
        self.assertEqual(self.lex.get_token(), (False, '9'))
    def test_get_token_number_inset(self):
        self.lex = LexParser('9')
        self.assertEqual(self.lex.get_token(inset=True), (False, '9'))
    def test_get_token_number_firstchar(self):
        self.lex = LexParser('9')
        self.assertEqual(self.lex.get_token(inset=True, firstchar=True), (False, '9'))

    def test_get_token_char(self):
        self.lex = LexParser('$')
        self.assertEqual(self.lex.get_token(), (False, '$'))
    def test_get_token_char_inset(self):
        self.lex = LexParser('$')
        self.assertEqual(self.lex.get_token(inset=True), (False, '$'))
    def test_get_token_char_firstchar(self):
        self.lex = LexParser('$')
        self.assertEqual(self.lex.get_token(inset=True, firstchar=True), (False, '$'))

    def test_get_token_operator(self):
        self.lex = LexParser('*')
        self.assertEqual(self.lex.get_token(), (True, '*'))
    def test_get_token_operator_inset(self):
        self.lex = LexParser('*')
        self.assertEqual(self.lex.get_token(inset=True), (False, '*'))
    def test_get_token_operator_firstchar(self):
        self.lex = LexParser('*')
        self.assertEqual(self.lex.get_token(inset=True, firstchar=True), (False, '*'))

    def test_get_token_escape(self):
        self.lex = LexParser('\\(')
        self.assertEqual(self.lex.get_token(), (False, '\\('))
    def test_get_token_escape_inset(self):
        self.lex = LexParser('\\(')
        self.assertEqual(self.lex.get_token(inset=True), (False, '\\('))
    def test_get_token_escape_firstchar(self):
        self.lex = LexParser('\\(')
        self.assertEqual(self.lex.get_token(inset=True, firstchar=True), (False, '\\('))

    def test_get_token_abbreviation(self):
        self.lex = LexParser('\\t')
        self.assertEqual(self.lex.get_token(), (False, '\\t'))
    def test_get_token_abbreviation_inset(self):
        self.lex = LexParser('\\t')
        self.assertEqual(self.lex.get_token(inset=True), (False, '\\t'))
    def test_get_token_abbreviation_firstchar(self):
        self.lex = LexParser('\\t')
        self.assertEqual(self.lex.get_token(inset=True, firstchar=True), (False, '\\t'))

    def test_get_token_mnemonic(self):
        self.lex = LexParser('\\w')
        self.assertEqual(self.lex.get_token(), (False, '\\w'))
    def test_get_token_mnemonic_inset(self):
        self.lex = LexParser('\\w')
        self.assertEqual(self.lex.get_token(inset=True), (False, '\\w'))
    def test_get_token_mnemonic_firstchar(self):
        self.lex = LexParser('\\w')
        self.assertEqual(self.lex.get_token(inset=True, firstchar=True), (False, '\\w'))

    def test_get_token_backslash(self):
        self.lex = LexParser('\\')
        self.assertEqual(self.lex.get_token(), (True, '\\'))
    def test_get_token_backslash_inset(self):
        self.lex = LexParser('\\')
        self.assertEqual(self.lex.get_token(inset=True), (True, '\\'))
    def test_get_token_backslash_firstchar(self):
        self.lex = LexParser('\\')
        self.assertEqual(self.lex.get_token(inset=True, firstchar=True), (True, '\\'))

    def test_get_token_eor(self):
        self.lex = LexParser('')
        self.assertEqual(self.lex.get_token(), (True, 'EOR'))
    def test_get_token_eor_inset(self):
        self.lex = LexParser('')
        self.assertEqual(self.lex.get_token(inset=True), (True, 'EOR'))
    def test_get_token_eor_firstchar(self):
        self.lex = LexParser('')
        self.assertEqual(self.lex.get_token(inset=True, firstchar=True), (True, 'EOR'))

    def test_get_token_all(self):
        self.lex = LexParser('(\\l%=\\f)|\\**\\\\\\')
        self.assertEqual(self.lex.get_token(), (True, '('))
        self.assertEqual(self.lex.get_token(), (False, '\\l'))
        self.assertEqual(self.lex.get_token(), (False, '%'))
        self.assertEqual(self.lex.get_token(), (False, '='))
        self.assertEqual(self.lex.get_token(), (False, '\\f'))
        self.assertEqual(self.lex.get_token(), (True, ')'))
        self.assertEqual(self.lex.get_token(), (True, '|'))
        self.assertEqual(self.lex.get_token(), (False, '\\*'))
        self.assertEqual(self.lex.get_token(), (True, '*'))
        self.assertEqual(self.lex.get_token(), (False, '\\\\'))
        self.assertEqual(self.lex.get_token(), (True, '\\'))
        self.assertEqual(self.lex.get_token(), (True, 'EOR'))

