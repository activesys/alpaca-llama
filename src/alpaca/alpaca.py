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
from options import OptionsError
from input import Input
from output import Output

class AlpacaError(Exception):
    pass

class Alpaca:
    def main():
        try:
            Options.parse(sys.argv[1:])
        except OptionsError as err:
            print(err.args[0])
            print()
            Alpaca.show_help()
            return

        if Options.is_show_help():
            Alpaca.show_help()
            return

        if Options.is_show_version():
            Alpaca.show_version()
            return

        Alpaca.translate_regex()

    def translate_regex():
        texts = Input.get_regexes()

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
        Output.output_script(dot.script)

    def show_version():
        print('alpaca.py 1.0.0')
        print('Copyright (C) 2013 activesys.wb@gmail.com')

    def show_help():
        print('USAGE')
        print('    alpaca.py [OPTION] [input-file]')
        print()
        print('DESCRIPTION')
        print('    alpaca.py translate regular expression to DFA, and output the DFA as DOT format.')
        print()
        print('OPTION')
        print('-o output-file')
        print('--output=output-file')
        print('    write output to \'output-file\', write output to stdout when this option not present.')
        print('-h')
        print('--help')
        print('    show this usage and exit.')
        print('-V')
        print('--version')
        print('    show copyright and version message and exit.')
        print()


if __name__ == '__main__':
    Alpaca.main()

