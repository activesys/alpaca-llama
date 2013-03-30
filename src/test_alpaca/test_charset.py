"""
test_charset.py

unittesting for Character Set
"""

import unittest
from charset import CharacterSet
from charset import CharacterSetError

class TestCharacterSet(unittest.TestCase):
    def test_is_valid_range(self):
        self.assertTrue(CharacterSet.is_valid_range('\\t', '!'))
        self.assertTrue(CharacterSet.is_valid_range('#', '#'))
        self.assertFalse(CharacterSet.is_valid_range('\\', '0'))
        self.assertRaises(CharacterSetError, CharacterSet.is_valid_range, 'abc', 'ddd')

    def test_intersection_set_one(self):
        cset = CharacterSet.intersection_set('a')
        self.assertEqual(cset, ['a'])
    def test_intersection_set_range(self):
        cset = CharacterSet.intersection_set('!', 'M')
        self.assertEqual(cset,
            ['!', '"', '#', '$', '%', '&', "'", '(', ')',
             '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
             '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])
    def test_intersection_set_all(self):
        cset = CharacterSet.intersection_set('\\a', '~')
        self.assertEqual(cset,
            ['\\a', '\\b', '\\t', '\\n', '\\v', '\\f', '\\r', '\\c', '!', '"', '#', '$', '%', '&', "'", '(', ')',
             '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
             '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', '{', '|', '}', '~'])
    def test_intersection_set_invalid_range(self):
        self.assertRaises(CharacterSetError, CharacterSet.intersection_set, 'z', 'a')

    def test_complementary_set_one(self):
        cset = CharacterSet.complementary_set('a')
        self.assertEqual(cset,
            ['\\a', '\\b', '\\t', '\\n', '\\v', '\\f', '\\r', '\\c', '!', '"', '#', '$', '%', '&', "'", '(', ')',
             '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
             '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', '{', '|', '}', '~'])
    def test_complementary_set_range(self):
        cset = CharacterSet.complementary_set('\\c', 'q')
        self.assertEqual(cset,
            ['\\a', '\\b', '\\t', '\\n', '\\v', '\\f', '\\r', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', '{', '|', '}', '~'])
    def test_complementary_set_all(self):
        cset = CharacterSet.complementary_set('\\a', '~')
        self.assertEqual(cset, [])
    def test_complementary_set_full(self):
        cset = CharacterSet.complementary_set_full(CharacterSet.intersection_set('a', 'z') + CharacterSet.intersection_set('X', 'Z') + ['\\t', '\\c', '#', '^'])
        self.assertEqual(cset,
            ['\\a', '\\b', '\\n', '\\v', '\\f', '\\r', '!', '"', '$', '%', '&', "'", '(', ')',
             '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
             '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', '[', '\\', ']', '_', '`', '{', '|', '}', '~'])
    def test_complementary_set_invalid_range(self):
        self.assertRaises(CharacterSetError, CharacterSet.complementary_set, '4', '\\n')

