"""
options.py
"""

import getopt
import sys

class Options:
    def __init__(self, args):
        try:
            optlist, args = getopt.getopt(args, 'o:')
        except getopt.GetoptErr as err:
            print(err)
            sys.exit(2)

        for option, value in optlist:
            if option == '-o':
                self.output_path = value
                break
        else:
            self.output_path = '-'

        if len(args) > 0:
            self.input_path = args[0]
        else:
            self.input_path = '-'

