"""
output.py
"""

import sys

class OutputError(Exception):
    pass
class OutputAbstractError(OutputError):
    pass
class PermissionDeniedError(OutputError):
    pass

class Output:
    def __init__(self):
        raise OutputAbstractError
    def write(self):
        raise OutputAbstractError

class FileOutput(Output):
    def __init__(self, path):
        try:
            self.__output_file = open(path, 'w')
        except IOError:
            raise PermissionDeniedError

    def write(self, contents):
        self.__output_file.writelines(contents)
        self.__output_file.close()

class ConsoleOutput(Output):
    def __init__(self):
        self.__console = sys.stdout

    def write(self, contents):
        self.__console.writelines(contents)

class OutputFactory:
    class __Instance:
        def create(self, path):
            if path == '-':
                return ConsoleOutput()
            else:
                return FileOutput(path)

    __instance = None

    def __init__(self):
        if not OutputFactory.__instance:
            OutputFactory.__instance = OutputFactory.__Instance()

    def __getattr__(self, attr):
        return getattr(OutputFactory.__instance, attr)
    def __setattr__(self, attr, value):
        return setattr(OutputFactory.__instance, attr, value)

