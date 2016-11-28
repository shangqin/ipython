from __future__ import print_function
import unittest

"""
id()
    Return the identity of an object.  This is guaranteed to be unique among
    simultaneously existing objects.  (Hint: it's the object's memory address.)
"""


class IDTest(unittest.TestCase):
    def test_none_id(self):
        a = None
        b = None
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertEqual(id(a), id(b))

    def test_bool_id(self):
        a = True
        b = False
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertNotEqual(id(a), id(b))

        a = True
        b = True
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertEqual(id(a), id(b))

        a = False
        b = False
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertEqual(id(a), id(b))

    def test_int_id(self):
        a = 1
        b = 2
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertNotEqual(id(a), id(b))

    def test_same_int_id(self):
        a = 1
        b = 1
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertEqual(id(a), id(b))

    def test_str_id(self):
        a = 'hello'
        b = 'world'
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertNotEqual(id(a), id(b))

    def test_empty_str_id(self):
        a = ''
        b = ''
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertEqual(id(a), id(b))

    def test_same_str_id(self):
        a = 'hello'
        b = 'hello'
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertEqual(id(a), id(b))

    def test_list_id(self):
        a = [1]
        b = [1, 2]
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertNotEqual(id(a), id(b))

    def test_empty_list_id(self):
        a = []
        b = []
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertNotEqual(id(a), id(b))

    def test_same_list_id(self):
        a = [1, 2]
        b = [1, 2]
        print('a: %s' % hex(id(a)))
        print('b: %s' % hex(id(b)))
        self.assertNotEqual(id(a), id(b))


if __name__ == '__main__':
    unittest.main()
