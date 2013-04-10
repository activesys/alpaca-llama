"""
options.py
Parser for command line options of alpaca.
"""

import getopt

class Options:
    # 'o' = output, '' = input
    options = {'o': None, '': None}

    def parse(optlist):
        opts, args = getopt.getopt(optlist, 'o:', ['output='])

        for opt, val in opts:
            if opt in ('-o', '--output'):
                Options.options['o'] = val.strip()

        if len(args) > 0:
            Options.options[''] = args[0].strip()

    def get_output():
        return Options.options['o']
    def get_input():
        return Options.options['']

