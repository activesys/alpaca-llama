"""
input.py
"""

class Input:
    def __init__(self, path):
        self.input_file = open(path, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.input_file).strip()

