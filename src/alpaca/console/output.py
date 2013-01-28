"""
output.py
"""

class Output:
    def __init__(self, path):
        self.output_file = open(path, 'w')

    def output(self, script):
        self.output_file.write(script)
        self.output_file.close()
