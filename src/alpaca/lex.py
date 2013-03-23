"""
lex.py

lexical parser.
"""

from table import StateTransitionTable

class RegexLexError(Exception):
    pass
class EndOfRegex(Exception):
    pass

class LexParser:
    def __init__(self, regex):
        self.regex = regex
        self.index = 0
        self.table = StateTransitionTable()

    def get_token(self):
        try:
            state = self.table.next_state(self.table.STATE_START, self.regex[self.index])
        except IndexError:
            raise EndOfRegex

        if state == self.table.STATE_FINISH:
            token = self.regex[self.index]
            self.index += 1
            return token
        else:
            try:
                state = self.table.next_state(state, self.regex[self.index+1])
            except IndexError:
                token = self.regex[self.index]
                self.index += 1
                return token
            else:
                if state == self.table.STATE_FINISH:
                    token = self.regex[self.index : self.index+2]
                    self.index += 2
                    return token
                else:
                    raise RegexLexError('Regex Lexical Error!')


