"""
test.py
"""

import sys
sys.path.append('../alpaca/')

import unittest
from test_table import TestStateTransitionTable
from test_lex import TestLexParser

if __name__ == '__main__':
    unittest.main(verbosity=2)

