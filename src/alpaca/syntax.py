"""
syntax.py

Syntax Pasrse for Regex
"""

from ast import AST
from lex import LexParser
from lex import EndOfRegex

class SyntaxParserError(Exception):
    pass

class SyntaxParser:
    def __init__(self, regex):
        self.root = AST()
        self.lex = LexParser(regex)

    def build(self):
        return __parse_regex()

    def __parse_regex(self):
        root = AST()
        try:
            self.token = self.lex.get_token()
        except EndOfRegex:
            raise SyntaxParserError('Regex Syntax Error: we need "(", ".", operand or "[", but we encount EndOfRegex!')
        else:
            # select(REGEX ::= SIMPLE UNION_ELR) = {'(', '.', operand, '['}
            if self.token[0] or self.token[1] in ['(', '.', '[']:
                root.children.append(__parse_simple())
                __parse_union_elr(root)
                return root
            else:
                raise SyntaxParserError('Regex Syntax Error: we need "(", ".", operand or "[", but we encount %s!' % self.token[1])

    def __parse_union_elr(self, root):
        # select(UNION_ELR ::= '|' SIMPLE UNION_ELR) = {'|'}
        # select(UNION_ELR ::= $) = {#, ')'}
        if self.token[1] is '|':
            root.operator = self.token[1]
            try:
                self.token = self.lex.get_token()
            except EndOfRegex:
                raise SyntaxParserError('Regex Syntax Error: we need "(", ".", operand or "[", but we encount EndOfRegex!')
            else:
                root.children.append(__parse_simple())
                __parse_union_elr(root)
        else:
            try:
                self.token = self.lex.get_token()
            except EndOfRegex:
                return
            else:
                if self.token[1] is ')':
                    return
                else:
                    raise SyntaxParserError('Regex Syntax Error: we need ")" or EndOfRegex, but we encount %s!' % self.token[1])

    def __parse_simple(self):
        # select(SIMPLE ::= BASIC CONCATENATION_ELR) = {'(', '.', operand, '['}
        if self.token[0] or self.token[1] in ['(', '.', '[']:
            root = AST()
            root.children.append(__parse_basic())
            __parse_concatenation_elr(root)
            return root
        else:
            raise SyntaxParserError('Regex Syntax Error: we need "(", ".", operand or "[", but we encount %s!' % self.token[1])

    def __parse_concatenation_elr(self, root):
        # select(CONCATENATION_ELR ::= BASIC CONCATENATION_ELR) = {'(', '.', operand, '['}
        # select(CONCATENATION_ELR ::= $) = {'|', #, ')'}
        if self.token[0] or self.token[1] in ['(', '.', '[']:
            root.childrend.append(__parse_basic())
            __parse_concatenation_elr(root)
        else if self.token[1] in ['|', ')']:
            return
        else:
            raise SyntaxParserError('Regex Syntax Error: we need "(", ".", operand, "[" and "|", ")", but we encount %s!' % self.token[1])

    def __parse_basic(self):
        # select(BASIC ::= ELEMENTARY BASIC_ECF) = {'(', '.', operand, '['}
        if self.token[0] or self.token[1] in ['(', '.', '[']:


