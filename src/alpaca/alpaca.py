#!/usr/bin/env python3

"""
alpaca.py
"""

import sys

from console import options
from console import input
from console import output
from bussiness import regex
from bussiness import nfa
from bussiness import dfa
from ts import dot

class Alpaca:
    def __init__(self, args):
        self.options = options.Options(args)
        self.input = input.Input(self.options.input_path)
        self.output = output.Output(self.options.output_path)
        self.regexs = [regex.Regex(line) for line in self.input]
        self.nfa = nfa.NFA(self.regexs)
        self.dfa = dfa.DFA(self.nfa)
        self.dot = dot.Dot(self.dfa)

        self.output.output(self.dot.script)


def main():
    alpaca = Alpaca(sys.argv[1:])


if __name__ == '__main__':
    main()
