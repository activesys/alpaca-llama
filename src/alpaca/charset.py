"""
charset.py

Character Set for Regex
"""

import string

class CharacterSetError(Exception):
    pass

class CharacterSet:
    set = [
        '\\a', '\\b', '\\t', '\\n', '\\v', '\\f', '\\r', '\\c', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
        '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
        '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
    ]
    mnemnoic = {
        '\\d': [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ],
        '\\D': [
            '\\a', '\\b', '\\t', '\\n', '\\v', '\\f', '\\r', '\\c', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
            '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^',
            '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
        ],
        '\\w': [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ],
        '\\W': [
            '\\a', '\\b', '\\t', '\\n', '\\v', '\\f', '\\r', '\\c', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
            '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~'
        ],
        '\\s': [
            '\\a', '\\b', '\\t', '\\n', '\\v', '\\f', '\\r', '\\c'
        ],
        '\\S': [
            '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5',
            '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
            '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
        ],
        '\\l': [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'
        ],
        '\\C': [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z'
        ]
    }

    def is_valid_range(self, begin, end):
        pos_begin, pos_end = CharacterSet.set.index(begin), CharacterSet.set.index(end)
        return pos_begin <= pos_end

    def intersection_set(self, begin, end=None):
        if begin not in CharacterSet.set or end != None and end not in CharacterSet.set:
            raise CharacterSetError

        if end != None and not self.is_valid_range(begin, end):
            raise CharacterSetError

        if end == None:
            return [begin]
        else:
            return CharacterSet.set[CharacterSet.set.index(begin) : CharacterSet.set.index(end)+1]

    def complementary_set(self, begin, end=None):
        if begin not in CharacterSet.set or end != None and end not in CharacterSet.set:
            raise CharacterSetError

        if end != None and not self.is_valid_range(begin, end):
            raise CharacterSet

        if end == None:
            return CharacterSet.set[:].remove(begin)
        else:
            set = CharacterSet.set[:]
            del set[CharacterSet.set.index(begin) : CharacterSet.set.index(end)+1]
            return set

