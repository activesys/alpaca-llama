"""
test.py
"""

import sys
sys.path.append('../alpaca/')

import unittest
from test_console.test_options import TestOptions

"""
def main():
    alltests = unittest.TestSuite([test_options.OptionsTestSuite])
    runner = unittest.TextTestRunner()
    runner.run(alltests)
"""

if __name__ == '__main__':
    unittest.main(verbosity=2)
