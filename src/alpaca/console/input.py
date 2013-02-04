"""
input.py
"""

import sys

class InputError(Exception):
    pass
class InputAbstractError(InputError):
    pass
class InvalidPathError(InputError):
    pass

class Input:
    def __init__(self):
        raise InputAbstractError
    def __iter__(self):
        raise InputAbstractError
    def __next__(self):
        raise InputAbstractError
    def __enter__(self):
        raise InputAbstractError
    def __exit__(self):
        raise InputAbstractError

class FileInput(Input):
    def __init__(self, path):
        try:
            self.__input_file = open(path, 'r')
        except IOError:
            raise InvalidPathError

    def __iter__(self):
        return self
    def __next__(self):
        return next(self.__input_file).strip()

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, tracebace):
        self.__input_file.close()

class ConsoleInput(Input):
    def __init__(self):
        self.__console = sys.stdin

    def __iter__(self):
        return self
    def __next__(self):
        return next(self.__console).strip()

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, tracebace):
        pass

class InputFactory:
    class __Instance:
        def create(self, path):
            if path == '-':
                return ConsoleInput()
            else:
                return FileInput(path)

    __instance = None

    def __init__(self):
        if not InputFactory.__instance:
            InputFactory.__instance = InputFactory.__Instance()

    def __getattr__(self, attr):
        return getattr(InputFactory.__instance, attr)
    def __setattr__(self, attr, value):
        return setattr(InputFactory.__instance, attr, value)

