from __future__ import print_function
from pprint import pprint
import unittest
import re

r"""
1, search() vs. match()
    1) re.match() checks for a match only at the beginning of the string
        while re.search() checks for a match anywhere in the string (this is what Perl does by default)
    2) in MULTILINE mode
        match() only matches at the beginning of the string
        search() with a regular expression beginning with '^' will match at the beginning of each line
2, re.MULTILINE
    1) '^' matches at the beginning of the string and at the beginning of each line (immediately following each newline)
    2) '$' matches at the end of the string and at the end of each line (immediately preceding each newline)
    By default, '^' matches only at the beginning of the string, and '$' only at the end of the string and immediately
    before the newline (if any) at the end of the string
"""


class ReTestCase(unittest.TestCase):
    def test_match(self):
        # Try to apply the pattern at the start of the string
        line = 'Cats are smarter than dogs'
        m = re.match(r'Cats', line)
        self.assertIsNotNone(m)
        print(m.group(0))

        m = re.match(r'smarter', line)
        self.assertIsNone(m)

        m = re.match(r'(.*) are (.*?) .*', line)
        self.assertIsNotNone(m)
        print(m.groups())
        print('m.group(0) is %s' % m.group(0))
        print('m.group(1) is %s' % m.group(1))
        print('m.group(2) is %s' % m.group(2))

    def test_search(self):
        # Scan through string looking for a match to the pattern
        # Search for first occurrence
        line = 'Cats are smarter than dogs'
        m = re.search(r'Cats', line)
        self.assertIsNotNone(m)
        print(m.group(0))

        m = re.search(r'smarter', line)
        self.assertIsNotNone(m)
        print(m.group(0))

        m = re.search(r'(.*) are (.*?) .*', line)
        self.assertIsNotNone(m)
        print(m.groups())
        print('m.group(0) is %s' % m.group(0))
        print('m.group(1) is %s' % m.group(1))
        print('m.group(2) is %s' % m.group(2))

    def test_findall(self):
        # Return a list of all non-overlapping matches in the string
        re.findall()

    def test_split(self):
        """
        Split the source string by the occurrences of the pattern
        1) split() splits a string into a list delimited by the passed pattern.
        2) The method is invaluable for converting textual data into data structures
            that can be easily read and modified by Python
        """

        text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronad Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""

        # 1, split by line
        entries = re.split(r'\n+', text)
        pprint(entries)
        self.assertEqual(len(entries), 4)

        # 2, split
        print('default maxsplit=0')
        details = [re.split(":? ", entry) for entry in entries]
        pprint(details)

        print('maxsplit=1')
        details = [re.split(":? ", entry, 1) for entry in entries]
        pprint(details)

        print('maxsplit=2')
        details = [re.split(":? ", entry, 2) for entry in entries]
        pprint(details)

        print('maxsplit=3')
        details = [re.split(":? ", entry, 3) for entry in entries]
        pprint(details)

        print('maxsplit=4')
        details = [re.split(":? ", entry, 4) for entry in entries]
        pprint(details)

    def test_sub(self):
        # Return the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string
        # by the replacement repl

        # 1, remove comment
        phone = '2004-959-559 # This is phone number'
        num = re.sub(r'#.*$', '', phone)
        self.assertRegexpMatches(num, r'^\d+-\d+-\d+\s+$')
        print('num is %s' % num)

        # 2, remove anything other than digits
        num = re.sub(r'\D', '', phone)
        self.assertRegexpMatches(num, r'^\d+$')
        print('num is %s' % num)

    def test_compile(self):
        # Compile a regular expression pattern, returning a pattern object
        pass

    def test_escape(self):
        pass


if __name__ == '__main__':
    unittest.main()
