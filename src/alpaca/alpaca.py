#!/usr/bin/env python3

"""
alpaca.py
Alpaca
"""

import sys
from regex import Regex
from regex import RegexError
from nfa import NFA
from dfa import DFA
from dot import Dot
from options import Options
from input import Input
from output import Output

class AlpacaError(Exception):
    pass

class Alpaca:
    def translate(texts):
        nfas = []
        try:
            for text in texts:
                regex = Regex(text)
                nfas.append(regex.transform())
        except RegexError as err:
            raise AlpacaError(err.args[0])

        nfa = NFA()
        nfa.merge(nfas)

        dfa = nfa.transform()
        dfa.minimize()

        dot = dfa.transform()
        return dot


if __name__ == '__main__':
    Options.parse(sys.argv[1:])
    texts = Input.get_regexes()
    dot = Alpaca.translate(texts)
    Output.output_script(dot.script)

