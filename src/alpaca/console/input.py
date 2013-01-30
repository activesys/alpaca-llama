"""
input.py
"""

class InputError(Exception):
    pass
class InvalidPathError(InputError):
    pass

class Input:
    def __init__(self):
        assert False, "Can't instantiate abstract class."
    def __iter__(self):
        assert False, "Abstract methods must be defined."
    def __next__(self):
        assert False, "Abstract methods must be defined."
    def __enter__(self):
        assert False, "Abstract methods must be defined."
    def __exit__(self):
        assert False, "Abstract methods must be defined."

class FileInput(Input):
    def __init__(self, path):
        try:
            self.input_file = open(path, 'r')
        except IOError:
            raise InvalidPathError

    def __iter__(self):
        return self
    def __next__(self):
        return next(self.input_file).strip()

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, tracebace):
        self.input_file.close()

