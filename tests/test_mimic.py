#!/usr/bin/env python3
"""
Unit tests for mimic assignment.

Students should not edit this file.
"""

import sys
import importlib
import unittest
import subprocess
from contextlib import redirect_stdout
from io import StringIO

# Kenzie devs: change this to 'soln.mimic' to test solution
PKG_NAME = 'mimic'

imdev = {
    '': ['I'],
    'I': ['am', "don't"],
    'a': ['software'],
    'am': ['a'],
    'and': ['I'],
    'care': ['who'],
    'developer,': ['and'],
    "don't": ['care'],
    'software': ['developer,'],
    'who': ['knows']
}


class TestMimic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested
        cls.module = importlib.import_module(PKG_NAME)

    def test_create_mimic_dict_1(self):
        """Check if create_mimic_dict returns a dict"""
        result = self.module.create_mimic_dict("imdev.txt")
        self.assertIsInstance(
            result, dict,
            "The return value of create_mimic_dict() should be a dict."
            )

    def test_create_mimic_dict_2(self):
        """Check if there is one entry for '' in the dict"""
        result = self.module.create_mimic_dict("imdev.txt")
        self.assertIn(
            '', result,
            "Mimic dict should have one key entry for empty string '' "
            )

    def test_create_mimic_dict_3(self):
        """Check if create_mimic_dict contains expected keys & values"""
        result = self.module.create_mimic_dict("imdev.txt")
        self.assertDictEqual(
            result, imdev,
            "Mimic dict output for imdev.txt does match expected contents"
            )

    def test_print_mimic(self):
        """Check if requested number of words are printed"""
        d = self.module.create_mimic_dict("imdev.txt")
        buffer = StringIO()
        with redirect_stdout(buffer):
            self.module.print_mimic_random(d, 243)
            output = buffer.getvalue()
        word_count = len(output.split())
        self.assertEqual(
            word_count, 243,
            "Requested num_words does not match actual printed word count"
            )

    def test_print_mimic_no_newlines(self):
        """Check that no newline characters are present in output"""
        d = self.module.create_mimic_dict("imdev.txt")
        buffer = StringIO()
        with redirect_stdout(buffer):
            self.module.print_mimic_random(d, 200)
        output = buffer.getvalue()
        self.assertNotIn(
            '\n', output,
            "There should not be any newline (\\n) characters in output"
            )

    def test_print_mimic_random(self):
        """Check that each print output is randomly different"""
        d = self.module.create_mimic_dict("imdev.txt")
        buffer = StringIO()
        with redirect_stdout(buffer):
            self.module.print_mimic_random(d, 100)
            output1 = buffer.getvalue()
        with redirect_stdout(buffer):
            self.module.print_mimic_random(d, 100)
            output2 = buffer.getvalue()
        self.assertNotEqual(
            output1, output2,
            "Each printed output should be randomly different"
            )

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)

    def test_author_string(self):
        """Checking for __author__ string"""
        self.assertNotEqual(self.module.__author__, '???')


if __name__ == '__main__':
    unittest.main()
