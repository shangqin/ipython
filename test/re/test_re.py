from __future__ import print_function
import unittest
import re


class ReTestCase(unittest.TestCase):
    def test_match(self):
        # Try to apply the pattern at the start of the string
        pass

    def test_search(self):
        # Scan through string looking for a match to the pattern
        pass

    def test_findall(self):
        # Return a list of all non-overlapping matches in the string
        pass

    def test_split(self):
        # Split the source string by the occurrences of the pattern
        pass

    def test_compile(self):
        # Compile a regular expression pattern, returning a pattern object
        pass

    def test_escape(self):
        pass


if __name__ == '__main__':
    unittest.main()
