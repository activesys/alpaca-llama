"""
test_syntax.py

unittesting for syntax parser.
"""

import unittest
from rast import RAST
from syntax import SyntaxParser
from syntax import SyntaxParserError

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

    #def test_build_error_union_clr(self):
        #self.syntax = SyntaxParser('a\\')
        #try:
            #self.syntax.build()
        #except SyntaxParserError as err:
            #msg = 'Regex Syntax Error: we need "|", ")" or EOR, but we encount "\\"!'
            #self.assertEqual(err.args[0], msg)
        #else:
            #self.assertTrue(False)


class TestSyntaxParser(unittest.TestCase):
    def test_build_basic(self):
        self.syntax = SyntaxParser('a')
        root = self.syntax.build()
        self.assertEqual(root.operator, 'a')
        self.assertEqual(len(root.children), 0)

    def test_build_pointer(self):
        self.syntax = SyntaxParser('.')
        root = self.syntax.build()
        self.assertEqual(root.operator, '.')
        self.assertEqual(len(root.children), 0)

    def test_build_group(self):
        self.syntax = SyntaxParser('(a)')
        root = self.syntax.build()
        self.assertEqual(root.operator, 'a')
        self.assertEqual(len(root.children), 0)

    def test_build_pset(self):
        self.syntax = SyntaxParser('[a]')
        root = self.syntax.build()
        self.assertEqual(root.operator, '[]')
        self.assertEqual(len(root.children), 1)
        self.assertEqual(root.children[0].operator, 'a')

    def test_build_nset(self):
        self.syntax = SyntaxParser('[^a]')
        root = self.syntax.build()
        self.assertEqual(root.operator, '[^]')
        self.assertEqual(len(root.children), 1)
        self.assertEqual(root.children[0].operator, 'a')

    def test_build_range(self):
        self.syntax = SyntaxParser('[^a-z]')
        root = self.syntax.build()
        self.assertEqual(root.operator, '[^]')
        self.assertEqual(len(root.children), 1)
        range = root.children[0]
        self.assertEqual(range.operator, '-')
        self.assertEqual(len(range.children), 2)
        self.assertEqual(range.children[0].operator, 'a')
        self.assertEqual(range.children[1].operator, 'z')

    def test_build_set(self):
        self.syntax = SyntaxParser('[^a-z0-9+\-*/(^)]')
        root = self.syntax.build()
        self.assertEqual(root.operator, '[^]')
        self.assertEqual(len(root.children), 9)

        elem = root.children[0]
        self.assertEqual(elem.operator, '-')
        self.assertEqual(len(elem.children), 2)
        self.assertEqual(elem.children[0].operator, 'a')
        self.assertEqual(elem.children[1].operator, 'z')

        elem = root.children[1]
        self.assertEqual(elem.operator, '-')
        self.assertEqual(len(elem.children), 2)
        self.assertEqual(elem.children[0].operator, '0')
        self.assertEqual(elem.children[1].operator, '9')

        elem = root.children[2]
        self.assertEqual(elem.operator, '+')
        self.assertEqual(len(elem.children), 0)

        elem = root.children[3]
        self.assertEqual(elem.operator, '\-')
        self.assertEqual(len(elem.children), 0)

        elem = root.children[4]
        self.assertEqual(elem.operator, '*')
        self.assertEqual(len(elem.children), 0)

        elem = root.children[5]
        self.assertEqual(elem.operator, '/')
        self.assertEqual(len(elem.children), 0)

        elem = root.children[6]
        self.assertEqual(elem.operator, '(')
        self.assertEqual(len(elem.children), 0)

        elem = root.children[7]
        self.assertEqual(elem.operator, '^')
        self.assertEqual(len(elem.children), 0)

        elem = root.children[8]
        self.assertEqual(elem.operator, ')')
        self.assertEqual(len(elem.children), 0)

    def test_build_kleene_closure(self):
        self.syntax = SyntaxParser('a*')
        root = self.syntax.build()
        self.assertEqual(root.operator, '*')
        self.assertEqual(len(root.children), 1)
        self.assertEqual(root.children[0].operator, 'a')
        self.assertEqual(len(root.children[0].children), 0)

    def test_build_positive_closure(self):
        self.syntax = SyntaxParser('a+')
        root = self.syntax.build()
        self.assertEqual(root.operator, '+')
        self.assertEqual(len(root.children), 1)
        self.assertEqual(root.children[0].operator, 'a')
        self.assertEqual(len(root.children[0].children), 0)

    def test_build_concatenation(self):
        self.syntax = SyntaxParser('ab')
        root = self.syntax.build()
        self.assertEqual(root.operator, '')
        self.assertEqual(len(root.children), 2)
        operand_a = root.children[0]
        operand_b = root.children[1]
        self.assertEqual(operand_a.operator, 'a')
        self.assertEqual(len(operand_a.children), 0)
        self.assertEqual(operand_b.operator, 'b')
        self.assertEqual(len(operand_b.children), 0)

    def test_build_union(self):
        self.syntax = SyntaxParser('a|b')
        root = self.syntax.build()
        self.assertEqual(root.operator, '|')
        self.assertEqual(len(root.children), 2)
        operand_a = root.children[0]
        operand_b = root.children[1]
        self.assertEqual(operand_a.operator, 'a')
        self.assertEqual(len(operand_a.children), 0)
        self.assertEqual(operand_b.operator, 'b')
        self.assertEqual(len(operand_b.children), 0)


