"""
options.py
"""

import getopt
import sys

class OptionsInvalidError(Exception):
    pass

class Options:
    class __Instance:
        def __init__(self):
            self.__input_file = '-'
            self.__output_file = '-'

        def register(self, args=[]):
            try:
                optlist, args = getopt.getopt(args, 'o:')
            except getopt.GetoptError:
                raise OptionsInvalidError()

            for option, value in optlist:
                if option == '-o':
                    self.__output_file = value
                    break
            else:
                self.__output_file = '-'

            if len(args) > 0:
                self.__input_file = args[0]
            else:
                self.__input_file = '-'

        def input_file(self):
            return self.__input_file
        def output_file(self):
            return self.__output_file

    __instance = None

    def __init__(self):
        if not Options.__instance:
            Options.__instance = Options.__Instance()

    def __getattr__(self, attr):
        return getattr(Options.__instance, attr)
    def __setattr__(self, attr, value):
        return setattr(Options.__instance, attr, value)

