"""
rast.py

Regex Abstract Syntax Tree
"""

class RAST:
    def __init__(self):
        self.is_operator = False
        self.token = ''
        self.children = []

    def is_empty(self):
        return not self.is_operator and self.token == '' and len(self.children) == 0

