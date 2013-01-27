"""
test_regex.py
"""

import unittest
from bussiness import regex

class TestRegex(unittest.TestCase):
    def setUp(self):
        self.regex = regex.Regex('regex')

    def test_regex(self):
        self.assertEqual(self.regex.regex, 'regex')
