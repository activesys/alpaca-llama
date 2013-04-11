"""
options.py
Parser for command line options of alpaca.
"""

import getopt

class OptionsError(Exception):
    pass

class Options:
    # 'o' = output, '' = input
    options = {'o': None, '': None, 'V': False, 'h': False}

    def parse(optlist):
        try:
            opts, args = getopt.getopt(optlist, 'o:Vh', ['output=', 'version', 'help'])
        except getopt.GetoptError as error:
            raise OptionsError("Invalid option '%s'" % error.opt)

        for opt, val in opts:
            if opt in ('-o', '--output'):
                Options.options['o'] = val.strip()
            elif opt in ('-V', '--version'):
                Options.options['V'] = True
            elif opt in ('-h', '--help'):
                Options.options['h'] = True

        if len(args) > 0:
            Options.options[''] = args[0].strip()

    def get_output():
        return Options.options['o']
    def get_input():
        return Options.options['']
    def is_show_version():
        return Options.options['V']
    def is_show_help():
        return Options.options['h']

