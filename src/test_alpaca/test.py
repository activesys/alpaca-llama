#!/usr/bin/env python3

"""
test.py
"""

import sys
sys.path.append('../alpaca/')

import unittest
from test_console.test_options import TestOptions
from test_console.test_input import TestFileInput
from test_console.test_output import TestOutput
from test_bussiness.test_regex import TestRegex

if __name__ == '__main__':
    unittest.main(verbosity=2)
