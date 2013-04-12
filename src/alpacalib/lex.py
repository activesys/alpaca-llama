"""
lex.py

lexical parser.
"""

from alpacalib.table import StateTransitionTable

class RegexLexError(Exception):
    pass


class TokenStrategy:
    def is_operator(self, char, inset=False, firstchar=False):
        # \ [ and ] are always operator in any case.
        if char in ['\\', '[', ']']:
            return True

        # - is operator in set, and operand in other case.
        if char == '-':
            return inset

        # ^ is operator in case that the ^ is first character in set.
        if char == '^':
            return inset and firstchar

        # | * + ( ) and . are not operator in set, and operator in other case.
        if char in ['|', '*', '+', '(', ')', '.']:
            return not inset

        # Other character is not operator in any case.
        return False


class LexParser:
    def __init__(self, regex):
        self.regex = regex
        self.index = 0
        self.table = StateTransitionTable()
        self.stragey = TokenStrategy()

    def get_token(self, inset=False, firstchar=False):
        try:
            state = self.table.next_state(self.table.STATE_START, self.regex[self.index])
        except IndexError:
            # EOR is special operator for End Of Regex.
            return (True, 'EOR')

        if state == self.table.STATE_FINISH:
            token = self.regex[self.index]
            self.index += 1
            return (self.stragey.is_operator(token, inset, firstchar), token)
        else:
            try:
                state = self.table.next_state(state, self.regex[self.index+1])
            except IndexError:
                token = self.regex[self.index]
                self.index += 1
                return (self.stragey.is_operator(token, inset, firstchar), token)
            else:
                if state == self.table.STATE_FINISH:
                    token = self.regex[self.index : self.index+2]
                    self.index += 2
                    return (self.stragey.is_operator(token, inset, firstchar), token)
                else:
                    raise RegexLexError('Regex Lexical Error!')


