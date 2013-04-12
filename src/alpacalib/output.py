"""
output.py
Output for output script
"""

import sys
import os.path
from alpacalib.options import Options

class OutputError(Exception):
    pass

class Output:
    def output_script(script):
        name = Options.get_output()

        try:
            output = None
            if name == None:
                output = sys.stdout
            else:
                output = open(os.path.expanduser(name), 'w')

            output.write(script)
        except OSError as err:
            raise OutputError('OutputError: %s' % str(err))

