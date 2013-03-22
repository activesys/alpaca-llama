"""
table.py

State transition table for lex parser.
"""

class StateTransitionTable:
    def __init__(self):
        self.table = {
            'START': {
                '\\': 'IN-ESCAPE',
                '|': 'FINISH', '*': 'FINISH', '+': 'FINISH', '(': 'FINISH', ')': 'FINISH', '.': 'FINISH',
                '^': 'FINISH', '[': 'FINISH', ']': 'FINISH', '-': 'FINISH', '0': 'FINISH', '1': 'FINISH',
                '2': 'FINISH', '3': 'FINISH', '4': 'FINISH', '5': 'FINISH', '6': 'FINISH', '7': 'FINISH',
                '8': 'FINISH', '9': 'FINISH', 'a': 'FINISH', 'b': 'FINISH', 'c': 'FINISH', 'd': 'FINISH',
                'e': 'FINISH', 'f': 'FINISH', 'g': 'FINISH', 'h': 'FINISH', 'i': 'FINISH', 'j': 'FINISH',
                'k': 'FINISH', 'l': 'FINISH', 'm': 'FINISH', 'n': 'FINISH', 'o': 'FINISH', 'p': 'FINISH',
                'q': 'FINISH', 'r': 'FINISH', 's': 'FINISH', 't': 'FINISH', 'u': 'FINISH', 'v': 'FINISH',
                'w': 'FINISH', 'x': 'FINISH', 'y': 'FINISH', 'z': 'FINISH', 'A': 'FINISH', 'B': 'FINISH',
                'C': 'FINISH', 'D': 'FINISH', 'E': 'FINISH', 'F': 'FINISH', 'G': 'FINISH', 'H': 'FINISH',
                'I': 'FINISH', 'J': 'FINISH', 'K': 'FINISH', 'L': 'FINISH', 'M': 'FINISH', 'N': 'FINISH',
                'O': 'FINISH', 'P': 'FINISH', 'Q': 'FINISH', 'R': 'FINISH', 'S': 'FINISH', 'T': 'FINISH',
                'U': 'FINISH', 'V': 'FINISH', 'W': 'FINISH', 'X': 'FINISH', 'Y': 'FINISH', 'Z': 'FINISH',
                '!': 'FINISH', '"': 'FINISH', '#': 'FINISH', '$': 'FINISH', '%': 'FINISH', '&': 'FINISH',
                "'": 'FINISH', ',': 'FINISH', '/': 'FINISH', ':': 'FINISH', ';': 'FINISH', '<': 'FINISH',
                '=': 'FINISH', '>': 'FINISH', '?': 'FINISH', '@': 'FINISH', '_': 'FINISH', '{': 'FINISH',
                '}': 'FINISH', '~': 'FINISH'
            },
            'IN-ESCAPE': {
                '|': 'FINISH', '*': 'FINISH', '+': 'FINISH', '(': 'FINISH', ')': 'FINISH', '.': 'FINISH',
                '^': 'FINISH', '[': 'FINISH', ']': 'FINISH', '-': 'FINISH', '\\': 'FINISH', 'a': 'FINISH',
                'b': 'FINISH', 'c': 'FINISH', 'f': 'FINISH', 'n': 'FINISH', 'r': 'FINISH', 't': 'FINISH',
                'v': 'FINISH', 'd': 'FINISH', 'D': 'FINISH', 'w': 'FINISH', 'W': 'FINISH', 's': 'FINISH',
                'S': 'FINISH', 'l': 'FINISH', 'C': 'FINISH'
            }
        }

    def next_state(self, state, char):
        try:
            next = self.table[state][char]
        except KeyError:
            return None
        else:
            return next

