#!/usr/bin/env python3

"""
alpaca.py
Alpaca
"""

import sys
from alpacalib.regex import Regex
from alpacalib.regex import RegexError
from alpacalib.nfa import NFA
from alpacalib.dfa import DFA
from alpacalib.dot import Dot
from alpacalib.options import Options
from alpacalib.options import OptionsError
from alpacalib.input import Input
from alpacalib.input import InputError
from alpacalib.output import Output
from alpacalib.output import OutputError

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
        texts = None
        try:
            texts = Input.get_regexes()
        except InputError as err:
            print(err.args[0], file=sys.stderr)
            return

        nfas = []
        for i in range(len(texts)):
            try:
                regex = Regex(texts[i])
                nfas.append(regex.transform())
            except RegexError as err:
                print('SyntaxError(%d): %s' % (i+1, err.args[0]))
                return
        nfa = NFA()
        nfa.merge(nfas)
        dfa = nfa.transform()
        dfa.minimize()
        dot = dfa.transform()

        try:
            Output.output_script(dot.script)
        except OutputError as err:
            print(err.args[0], file=sys.stderr)
            return

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
        print('input-file')
        print('    read input from \'input-file\', read input from stdin when \'input-file\' not present.')
        print()


if __name__ == '__main__':
    Alpaca.main()

