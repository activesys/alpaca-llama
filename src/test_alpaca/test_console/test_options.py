"""
test_options.py
"""

import unittest
from console import options

class TestOptions(unittest.TestCase):
    def setUp(self):
        self.options = options.Options()

    def test_get_input_path(self):
        path = self.options.get_input_path()
        self.assertEqual(path, '.')

    def test_get_output_style(self):
        style = self.options.get_output_style()
        self.assertEqual(style, 'dot')

"""
OptionsTestSuite = unittest.TestSuite()
OptionsTestSuite.addTest(TestOptions('test_get_input_path'))
OptionsTestSuite.addTest(TestOptions('test_get_output_style'))
"""
