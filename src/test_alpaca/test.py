#!/usr/bin/env python3

"""
test.py
"""

import sys
import pdb
sys.path.append('../alpaca/')

import unittest
from test_table import TestStateTransitionTable
from test_lex import TestLexParser
from test_lex import TestTokenStrategy
from test_syntax import TestSyntaxParser
from test_syntax import TestSyntaxParserError

if __name__ == '__main__':
    unittest.main(verbosity=2)

