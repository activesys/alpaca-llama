"""
test_syntax.py

unittesting for syntax parser.
"""

import unittest
from alpaca.rast import RAST
from alpaca.syntax import SyntaxParser
from alpaca.syntax import SyntaxParserError

class TestSyntaxParserError(unittest.TestCase):
    def test_build_error_empty(self):
        self.syntax = SyntaxParser('')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Syntax Error: we need "(", ".", "[" or operand, but we encount "EOR"!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)

    def test_build_error_regex(self):
        self.syntax = SyntaxParser('*')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Syntax Error: we need "(", ".", "[" or operand, but we encount "*"!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)

    def test_build_error_redundancy(self):
        self.syntax = SyntaxParser('a)')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Syntax Error: we need EOR, but we encount ")"!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)

    def test_build_error_group_missing_right_parenthesis(self):
        self.syntax = SyntaxParser('(a')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Syntax Error: we need ")", but we encount "EOR"!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)

    def test_build_error_set_firstchar(self):
        self.syntax = SyntaxParser('[-a]')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Syntax Error: we need "^" or operand, but we encount "-"!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)

    def test_build_error_set_missing_right_brackets(self):
        self.syntax = SyntaxParser('[a')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Syntax Error: we need "-", "]" or operand, but we encount "EOR"!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)

    def test_build_error_pset_empty(self):
        self.syntax = SyntaxParser('[]')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Syntax Error: we need "^" or operand, but we encount "]"!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)

    def test_build_error_nset_empty(self):
        self.syntax = SyntaxParser('[^]')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Syntax Error: we need operand, but we encount "]"!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)

    def test_build_error_range(self):
        self.syntax = SyntaxParser('[a--]')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Syntax Error: we need operand, but we encount "-"!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)

    def test_build_error_range_semantics_mnemonic(self):
        self.syntax = SyntaxParser('[\d-a]')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Semantics Error: we encount "\\d" in range!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)

    def test_build_error_range_semantics(self):
        self.syntax = SyntaxParser('[z-a]')
        try:
            self.syntax.build()
        except SyntaxParserError as err:
            msg = 'Regex Semantics Error: we encount a invalid range "z-a"!'
            self.assertEqual(err.args[0], msg)
        else:
            self.assertTrue(False)


class TestSyntaxParser(unittest.TestCase):
    def test_build_basic(self):
        self.syntax = SyntaxParser('a')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (False, 'a'))
        self.assertEqual(len(root.children), 0)

    def test_build_pointer(self):
        self.syntax = SyntaxParser('.')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (True, '.'))
        self.assertEqual(len(root.children), 0)

    def test_build_group(self):
        self.syntax = SyntaxParser('(a)')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (False, 'a'))
        self.assertEqual(len(root.children), 0)

    def test_build_pset(self):
        self.syntax = SyntaxParser('[a]')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (True, '[]'))
        self.assertEqual(len(root.children), 1)
        self.assertEqual((root.children[0].is_operator, root.children[0].token), (False, 'a'))

    def test_build_nset(self):
        self.syntax = SyntaxParser('[^a]')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (True, '[^]'))
        self.assertEqual(len(root.children), 1)
        self.assertEqual((root.children[0].is_operator, root.children[0].token), (False, 'a'))

    def test_build_range(self):
        self.syntax = SyntaxParser('[^a-z]')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (True, '[^]'))
        self.assertEqual(len(root.children), 1)
        range = root.children[0]
        self.assertEqual((range.is_operator, range.token), (True, '-'))
        self.assertEqual(len(range.children), 2)
        self.assertEqual((range.children[0].is_operator, range.children[0].token), (False, 'a'))
        self.assertEqual((range.children[1].is_operator, range.children[1].token), (False, 'z'))

    def test_build_set(self):
        self.syntax = SyntaxParser('[^a-z0-9+\-*/(^)]')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (True, '[^]'))
        self.assertEqual(len(root.children), 9)

        elem = root.children[0]
        self.assertEqual((elem.is_operator, elem.token), (True, '-'))
        self.assertEqual(len(elem.children), 2)
        self.assertEqual((elem.children[0].is_operator, elem.children[0].token), (False, 'a'))
        self.assertEqual((elem.children[1].is_operator, elem.children[1].token), (False, 'z'))

        elem = root.children[1]
        self.assertEqual((elem.is_operator, elem.token), (True, '-'))
        self.assertEqual(len(elem.children), 2)
        self.assertEqual((elem.children[0].is_operator, elem.children[0].token), (False, '0'))
        self.assertEqual((elem.children[1].is_operator, elem.children[1].token), (False, '9'))

        elem = root.children[2]
        self.assertEqual((elem.is_operator, elem.token), (False, '+'))
        self.assertEqual(len(elem.children), 0)

        elem = root.children[3]
        self.assertEqual((elem.is_operator, elem.token), (False, '\-'))
        self.assertEqual(len(elem.children), 0)

        elem = root.children[4]
        self.assertEqual((elem.is_operator, elem.token), (False, '*'))
        self.assertEqual(len(elem.children), 0)

        elem = root.children[5]
        self.assertEqual((elem.is_operator, elem.token), (False, '/'))
        self.assertEqual(len(elem.children), 0)

        elem = root.children[6]
        self.assertEqual((elem.is_operator, elem.token), (False, '('))
        self.assertEqual(len(elem.children), 0)

        elem = root.children[7]
        self.assertEqual((elem.is_operator, elem.token), (False, '^'))
        self.assertEqual(len(elem.children), 0)

        elem = root.children[8]
        self.assertEqual((elem.is_operator, elem.token), (False, ')'))
        self.assertEqual(len(elem.children), 0)

    def test_build_kleene_closure(self):
        self.syntax = SyntaxParser('a*')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (True, '*'))
        self.assertEqual(len(root.children), 1)
        self.assertEqual((root.children[0].is_operator, root.children[0].token), (False, 'a'))
        self.assertEqual(len(root.children[0].children), 0)

    def test_build_positive_closure(self):
        self.syntax = SyntaxParser('a+')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (True, '+'))
        self.assertEqual(len(root.children), 1)
        self.assertEqual((root.children[0].is_operator, root.children[0].token), (False, 'a'))
        self.assertEqual(len(root.children[0].children), 0)

    def test_build_concatenation(self):
        self.syntax = SyntaxParser('ab')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (True, ''))
        self.assertEqual(len(root.children), 2)
        operand_a = root.children[0]
        operand_b = root.children[1]
        self.assertEqual((operand_a.is_operator, operand_a.token), (False, 'a'))
        self.assertEqual(len(operand_a.children), 0)
        self.assertEqual((operand_b.is_operator, operand_b.token), (False, 'b'))
        self.assertEqual(len(operand_b.children), 0)

    def test_build_union(self):
        self.syntax = SyntaxParser('a|b')
        root = self.syntax.build()
        self.assertEqual((root.is_operator, root.token), (True, '|'))
        self.assertEqual(len(root.children), 2)
        operand_a = root.children[0]
        operand_b = root.children[1]
        self.assertEqual((operand_a.is_operator, operand_a.token), (False, 'a'))
        self.assertEqual(len(operand_a.children), 0)
        self.assertEqual((operand_b.is_operator, operand_b.token), (False, 'b'))
        self.assertEqual(len(operand_b.children), 0)


