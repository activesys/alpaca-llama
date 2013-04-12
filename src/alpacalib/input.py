"""
input.py
Input for regex input
"""

import sys
from alpacalib.options import Options

class InputError(Exception):
    pass

class Input:
    def get_regexes():
        name = Options.get_input()
        try:
            input = None
            if name == None:
                input = sys.stdin
            else:
                input = open(name, 'r')

            return [line.strip() for line in input]
        except OSError as err:
            raise InputError('InputError: %s' % str(err))

