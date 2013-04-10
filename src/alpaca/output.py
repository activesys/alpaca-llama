"""
output.py
Output for output script
"""

import sys
from options import Options

class Output:
    def output_script(script):
        name = Options.get_output()
        output = None
        if name == None:
            output = sys.stdout
        else:
            output = open(name, 'w')

        output.write(script)

