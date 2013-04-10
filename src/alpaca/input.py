"""
input.py
Input for regex input
"""

import sys
from options import Options

class Input:
    def get_regexes():
        name = Options.get_input()
        input = None
        if name == None:
            input = sys.stdin
        else:
            input = open(name, 'r')

        return [line.strip() for line in input]

