"""
rast.py

Regex Abstract Syntax Tree
"""

class RAST:
    def __init__(self):
        self.operator = ''
        self.children = []

    def is_empty(self):
        return self.operator is '' and len(self.children) == 0

