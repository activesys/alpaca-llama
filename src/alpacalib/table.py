"""
table.py

State transition table for lex parser.
"""

class StateTransitionTable:
    def __init__(self):
        self.STATE_START = 'START'
        self.STATE_IN_ESCAPE = 'IN-ESCAPE'
        self.STATE_FINISH = 'FINISH'
        self.table = {
            self.STATE_START: {
                '\\': 'IN-ESCAPE',
                '|': self.STATE_FINISH, '*': self.STATE_FINISH, '+': self.STATE_FINISH, '(': self.STATE_FINISH,
                ')': self.STATE_FINISH, '.': self.STATE_FINISH, '^': self.STATE_FINISH, '[': self.STATE_FINISH,
                ']': self.STATE_FINISH, '-': self.STATE_FINISH, '0': self.STATE_FINISH, '1': self.STATE_FINISH,
                '2': self.STATE_FINISH, '3': self.STATE_FINISH, '4': self.STATE_FINISH, '5': self.STATE_FINISH,
                '6': self.STATE_FINISH, '7': self.STATE_FINISH, '8': self.STATE_FINISH, '9': self.STATE_FINISH,
                'a': self.STATE_FINISH, 'b': self.STATE_FINISH, 'c': self.STATE_FINISH, 'd': self.STATE_FINISH,
                'e': self.STATE_FINISH, 'f': self.STATE_FINISH, 'g': self.STATE_FINISH, 'h': self.STATE_FINISH,
                'i': self.STATE_FINISH, 'j': self.STATE_FINISH, 'k': self.STATE_FINISH, 'l': self.STATE_FINISH,
                'm': self.STATE_FINISH, 'n': self.STATE_FINISH, 'o': self.STATE_FINISH, 'p': self.STATE_FINISH,
                'q': self.STATE_FINISH, 'r': self.STATE_FINISH, 's': self.STATE_FINISH, 't': self.STATE_FINISH,
                'u': self.STATE_FINISH, 'v': self.STATE_FINISH, 'w': self.STATE_FINISH, 'x': self.STATE_FINISH,
                'y': self.STATE_FINISH, 'z': self.STATE_FINISH, 'A': self.STATE_FINISH, 'B': self.STATE_FINISH,
                'C': self.STATE_FINISH, 'D': self.STATE_FINISH, 'E': self.STATE_FINISH, 'F': self.STATE_FINISH,
                'G': self.STATE_FINISH, 'H': self.STATE_FINISH, 'I': self.STATE_FINISH, 'J': self.STATE_FINISH,
                'K': self.STATE_FINISH, 'L': self.STATE_FINISH, 'M': self.STATE_FINISH, 'N': self.STATE_FINISH,
                'O': self.STATE_FINISH, 'P': self.STATE_FINISH, 'Q': self.STATE_FINISH, 'R': self.STATE_FINISH,
                'S': self.STATE_FINISH, 'T': self.STATE_FINISH, 'U': self.STATE_FINISH, 'V': self.STATE_FINISH,
                'W': self.STATE_FINISH, 'X': self.STATE_FINISH, 'Y': self.STATE_FINISH, 'Z': self.STATE_FINISH,
                '!': self.STATE_FINISH, '"': self.STATE_FINISH, '#': self.STATE_FINISH, '$': self.STATE_FINISH,
                '%': self.STATE_FINISH, '&': self.STATE_FINISH, "'": self.STATE_FINISH, ',': self.STATE_FINISH,
                '/': self.STATE_FINISH, ':': self.STATE_FINISH, ';': self.STATE_FINISH, '<': self.STATE_FINISH,
                '=': self.STATE_FINISH, '>': self.STATE_FINISH, '?': self.STATE_FINISH, '@': self.STATE_FINISH,
                '`': self.STATE_FINISH, '_': self.STATE_FINISH, '{': self.STATE_FINISH, '}': self.STATE_FINISH,
                '~': self.STATE_FINISH
            },
            self.STATE_IN_ESCAPE: {
                '|': self.STATE_FINISH, '*': self.STATE_FINISH, '+': self.STATE_FINISH, '(': self.STATE_FINISH,
                ')': self.STATE_FINISH, '.': self.STATE_FINISH, '^': self.STATE_FINISH, '[': self.STATE_FINISH,
                ']': self.STATE_FINISH, '-': self.STATE_FINISH, '\\': self.STATE_FINISH, 'a': self.STATE_FINISH,
                'b': self.STATE_FINISH, 'c': self.STATE_FINISH, 'f': self.STATE_FINISH, 'n': self.STATE_FINISH,
                'r': self.STATE_FINISH, 't': self.STATE_FINISH, 'v': self.STATE_FINISH, 'd': self.STATE_FINISH,
                'D': self.STATE_FINISH, 'w': self.STATE_FINISH, 'W': self.STATE_FINISH, 's': self.STATE_FINISH,
                'S': self.STATE_FINISH, 'l': self.STATE_FINISH, 'C': self.STATE_FINISH
            }
        }

    def next_state(self, state, char):
        try:
            next = self.table[state][char]
        except KeyError:
            return None
        else:
            return next

