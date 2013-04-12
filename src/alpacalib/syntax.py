"""
syntax.py

Syntax Pasrse for Regex
"""

from alpacalib.rast import RAST
from alpacalib.lex import LexParser
from alpacalib.charset import CharacterSet

class SyntaxParserError(Exception):
    pass

class SyntaxParser:
    def __init__(self, regex):
        self.lex = LexParser(regex)

    def build(self):
        self.root = self.__parse_regex()
        # check redundancy character.
        if not self.token[0] or self.token[1] != 'EOR':
            raise SyntaxParserError(
                'Regex Syntax Error: we need EOR, but we encount "%s"!'
                % self.token[1])

        return self.root

    def __parse_regex(self):
        self.token = self.lex.get_token()

        # select(REGEX ::= SIMPLE UNION_ELR) = {'(', '.', operand, '['}
        if not self.token[0] or self.token[1] in ['(', '.', '[']:
            elem = self.__parse_simple()
            root = RAST()
            self.__parse_union_elr(root)
            if not root.is_empty():
                root.children.insert(0, elem)
                return root
            else:
                return elem
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "(", ".", "[" or operand, but we encount "%s"!'
                % self.token[1])

    def __parse_union_elr(self, root):
        # select(UNION_ELR ::= '|' SIMPLE UNION_ELR) = {'|'}
        # select(UNION_ELR ::= $) = {#, ')'}
        if self.token[0] and self.token[1] == '|':
            root.is_operator, root.token = self.token
            self.token = self.lex.get_token()
            root.children.append(self.__parse_simple())
            self.__parse_union_elr(root)
        elif self.token[0] and self.token[1] in [')', 'EOR']:
            return
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "|", ")" or EOR, but we encount "%s"!'
                % self.token[1])

    def __parse_simple(self):
        # select(SIMPLE ::= BASIC CONCATENATION_ELR) = {'(', '.', operand, '['}
        if not self.token[0] or self.token[1] in ['(', '.', '[']:
            elem = self.__parse_basic()
            root = RAST()
            self.__parse_concatenation_elr(root)
            if not root.is_empty():
                root.children.insert(0, elem)
                return root
            else:
                return elem
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "(", ".", "[" or operand, but we encount "%s"!'
                % self.token[1])

    def __parse_concatenation_elr(self, root):
        # select(CONCATENATION_ELR ::= BASIC CONCATENATION_ELR) = {'(', '.', operand, '['}
        # select(CONCATENATION_ELR ::= $) = {'|', #, ')'}
        if not self.token[0] or self.token[1] in ['(', '.', '[']:
            root.is_operator = True
            root.children.append(self.__parse_basic())
            self.__parse_concatenation_elr(root)
        elif self.token[0] and self.token[1] in ['|', ')', 'EOR']:
            return
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "(", ".", "[", operand or "|", ")", EOR, but we encount "%s"!'
                % self.token[1])

    def __parse_basic(self):
        # select(BASIC ::= ELEMENTARY BASIC_ECF) = {'(', '.', operand, '['}
        if not self.token[0] or self.token[1] in ['(', '.', '[']:
            elem = self.__parse_elementary()
            root = self.__parse_basic_ecf()
            if not root.is_empty():
                root.children.append(elem)
                return root
            else:
                return elem

    def __parse_basic_ecf(self):
        # select(BASIC_ECF ::= '*') = {'*'}
        # select(BASIC_ECF ::= '+') = {'+'}
        # select(BASIC_ECF ::= empty) = {'(', '.', operand, '[', '|', eor, ')'}
        root = RAST()
        if self.token[0] and self.token[1] in ['*', '+']:
            root.is_operator, root.token = self.token
            self.token = self.lex.get_token()
            return root
        elif not self.token[0] or self.token[1] in ['(', '.', '[', '|', ')', 'EOR']:
            return root
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "(", ".", "[", operand or "|", ")", EOR, but we encount "%s"!'
                % self.token[1])

    def __parse_elementary(self):
        # select(ELEMENTARY :: = GROUP) = {'('}
        # select(ELEMENTARY ::= SET) = {'['}
        # select(ELEMENTARY ::= '.') = {'.'}
        # select(ELEMENTARY ::= operand) = {operand}
        if self.token[0] and self.token[1] == '(':
            return self.__parse_group()
        elif self.token[0] and self.token[1] == '[':
            return self.__parse_set()
        elif not self.token[0] or self.token[1] == '.':
            root = RAST()
            root.is_operator, root.token = self.token
            self.token = self.lex.get_token()
            return root
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "(", ".", "[" or operand, but we encount "%s"!'
                % self.token[1])

    def __parse_group(self):
        # select(GROUP ::= '(' REGEX ')') = {'('}
        if self.token[0] and self.token[1] == '(':
            root = self.__parse_regex()
            if self.token[0] and self.token[1] == ')':
                self.token = self.lex.get_token()
            else:
                raise SyntaxParserError(
                    'Regex Syntax Error: we need ")", but we encount "%s"!'
                    % self.token[1])
            return root
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "(", but we encount "%s"!'
                % self.token[1])

    def __parse_set(self):
        # select(SET ::= '[' SET_ECF) = {'['}
        if self.token[0] and self.token[1] == '[':
            root = RAST()
            root.is_operator, root.token = self.token
            self.token = self.lex.get_token(inset=True, firstchar=True)
            self.__parse_set_ecf(root)
            return root
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "[", but we encount "%s"!'
                % self.token[1])

    def __parse_set_ecf(self, root):
        # select(SET_ECF ::= ITEMS ']') = {operand}
        # select(SET_ECF ::= '^' ITEMS ']') = {'^'}
        if not self.token[0]:
            self.__parse_items(root)
        elif self.token[0] and self.token[1] == '^':
            root.is_operator = self.token[0]
            root.token += self.token[1]
            self.token = self.lex.get_token(inset=True)
            self.__parse_items(root)
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "^" or operand, but we encount "%s"!'
                % self.token[1])

        if self.token[0] and self.token[1] == ']':
            root.is_operator = self.token[0]
            root.token += self.token[1]
            self.token = self.lex.get_token()
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "]", but we encount "%s"!'
                % self.token[1])

    def __parse_items(self, root):
        # select(ITEMS ::= ITEM ITEMS_ECF) = {operand}
        if not self.token[0]:
            root.children.append(self.__parse_item())
            self.__parse_items_ecf(root)
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need operand, but we encount "%s"!'
                % self.token[1])

    def __parse_items_ecf(self, root):
        # select(ITEMS_ECF ::= ITEMS) = {operand}
        # select(ITEMS_ECF ::= empty) = {']'}
        if not self.token[0]:
            self.__parse_items(root)
        elif self.token[0] and self.token[1] == ']':
            return
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "]" or operand, but we encount "%s"!'
                % self.token[1])

    def __parse_item(self):
        # select(ITEM ::= operand ITEM_ECF) = {operand}
        if not self.token[0]:
            elem = RAST()
            elem.is_operator, elem.token = self.token
            self.token = self.lex.get_token(inset=True)
            root = self.__parse_item_ecf()
            if not root.is_empty():
                root.children.insert(0, elem)
                # We got a range, check validity of the range now.
                if root.children[0].token in CharacterSet.mnemnoic:
                    raise SyntaxParserError(
                        'Regex Semantics Error: we encount "%s" in range!'
                        % root.children[0].token)
                elif root.children[1].token in CharacterSet.mnemnoic:
                    raise SyntaxParserError(
                        'Regex Semantics Error: we encount "%s" in range!'
                        % root.children[1].token)
                elif CharacterSet.is_valid_range(root.children[0].token, root.children[1].token):
                    return root
                else:
                    raise SyntaxParserError(
                        'Regex Semantics Error: we encount a invalid range "%s%s%s"!'
                        % (root.children[0].token, root.token, root.children[1].token))
            else:
                return elem
        else: 
            raise SyntaxParserError(
                'Regex Syntax Error: we need operand, but we encount "%s"!'
                % self.token[1])

    def __parse_item_ecf(self):
        # select(ITEM_ECF ::= '-' operand) = {'-'}
        # select(ITEM_ECF ::= empty) = {operand, ']'}
        root = RAST()
        if self.token[0] and self.token[1] == '-':
            root.is_operator, root.token = self.token
            self.token = self.lex.get_token(inset=True)
            if not self.token[0]:
                elem = RAST()
                elem.is_operator, elem.token = self.token
                root.children.append(elem)
                self.token = self.lex.get_token(inset=True)
                return root
            else:
                raise SyntaxParserError(
                    'Regex Syntax Error: we need operand, but we encount "%s"!'
                    % self.token[1])
        elif not self.token[0] or self.token[1] == ']':
            return root
        else:
            raise SyntaxParserError(
                'Regex Syntax Error: we need "-", "]" or operand, but we encount "%s"!'
                % self.token[1])

