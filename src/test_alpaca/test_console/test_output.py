"""
test_output.py
"""

import unittest
from console import output

class TestFileOutput(unittest.TestCase):
    def test_PermissionDeniedError(self):
        self.assertRaises(output.PermissionDeniedError, output.FileOutput, '/root/file')

    def test_write(self):
        contents = ['Write data to output.dot\n'] * 4
        file_output = output.FileOutput('./data/output.dot')
        file_output.write(contents)
        with open('./data/output.dot', 'r') as file_input:
            for line in file_input:
                self.assertEqual(line.strip(), 'Write data to output.dot')

class TestConsoleOutput(unittest.TestCase):
    def test_write(self):
        contents = ['Write data to output.dot\n'] * 4
        console_output = output.ConsoleOutput()
        console_output.write(contents)
        with open('./data/stdout.output', 'r') as file_input:
            for line in file_input:
                self.assertEqual(line.strip(), 'Write data to output.dot')

class TestOutputFactory(unittest.TestCase):
    def test_PermissionDeniedError(self):
        self.assertRaises(output.PermissionDeniedError, output.OutputFactory().create, '/root/file')

    def test_create_fileoutput(self):
        file_output = output.OutputFactory().create('./data/output.dot')
        self.assertTrue(isinstance(file_output, output.FileOutput))
        file_output.write([])

    def test_create_consoleoutput(self):
        console_output = output.OutputFactory().create('-')
        self.assertTrue(isinstance(console_output, output.ConsoleOutput))

