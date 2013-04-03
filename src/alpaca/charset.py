"""
charset.py

Character Set for Regex
"""

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

    def is_valid_range(begin, end):
        if begin not in CharacterSet.set or end not in CharacterSet.set:
            raise CharacterSetError

        pos_begin, pos_end = CharacterSet.set.index(begin), CharacterSet.set.index(end)
        return pos_begin <= pos_end

    def intersection_set(begin, end=None):
        if begin not in CharacterSet.set or end != None and end not in CharacterSet.set:
            raise CharacterSetError

        if end != None and not CharacterSet.is_valid_range(begin, end):
            raise CharacterSetError

        if end == None:
            return [begin]
        else:
            return CharacterSet.set[CharacterSet.set.index(begin) : CharacterSet.set.index(end)+1]

    def complementary_set(begin, end=None):
        if begin not in CharacterSet.set or end != None and end not in CharacterSet.set:
            raise CharacterSetError

        if end != None and not CharacterSet.is_valid_range(begin, end):
            raise CharacterSetError

        if end == None:
            cset = CharacterSet.set[:]
            cset.remove(begin)
            return cset
        else:
            cset = CharacterSet.set[:]
            del cset[CharacterSet.set.index(begin) : CharacterSet.set.index(end)+1]
            return cset

    def complementary_set_full(clist):
        cset = CharacterSet.set[:]
        for char in clist:
            cset.remove(char)
        return cset

