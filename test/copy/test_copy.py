from __future__ import print_function
import unittest
import copy


def print_object(obj, comment):
    print(comment)
    print(obj)
    print('id is %s' % id(obj))
    print('element id is %s\n' % [id(e) for e in obj])


class CopyTestCase(unittest.TestCase):
    def test_copy(self):
        will = ["Will", 28, ["Python", "C#", "JavaScript"]]
        wilber = will  # same object
        print_object(will, 'will info:')
        print_object(wilber, 'wilber info:')

        self.assertEqual(will, wilber)
        self.assertEqual(id(will), id(wilber))
        self.assertEqual(id(will[0]), id(wilber[0]))
        self.assertEqual(id(will[1]), id(wilber[1]))
        self.assertEqual(id(will[2]), id(wilber[2]))

        print('#' * 20)

        will[0] = "Wilber"
        will[1] = 30
        will[2].append("CSS")
        print_object(will, 'will info:')
        print_object(wilber, 'wilber info:')

        self.assertEqual(will, wilber)
        self.assertEqual(id(will), id(wilber))
        self.assertEqual(id(will[0]), id(wilber[0]))
        self.assertEqual(id(will[1]), id(wilber[1]))
        self.assertEqual(id(will[2]), id(wilber[2]))

    def test_shallow_copy(self):
        will = ["Will", 28, ["Python", "C#", "JavaScript"]]
        wilber = copy.copy(will)  # different object
        print_object(will, 'will info:')
        print_object(wilber, 'wilber info:')

        self.assertEqual(will, wilber)
        self.assertNotEqual(id(will), id(wilber))
        self.assertEqual(id(will[0]), id(wilber[0]))
        self.assertEqual(id(will[1]), id(wilber[1]))
        self.assertEqual(id(will[2]), id(wilber[2]))

        print('#' * 20)

        will[0] = "Wilber"
        will[1] = 30
        will[2].append("CSS")
        print_object(will, 'will info:')
        print_object(wilber, 'wilber info:')

        self.assertNotEqual(will, wilber)
        self.assertNotEqual(id(will), id(wilber))

        # for immutable object, new object will be created
        # for mutable object, no new object will be created
        self.assertNotEqual(id(will[0]), id(wilber[0]))
        self.assertNotEqual(id(will[1]), id(wilber[1]))
        self.assertEqual(id(will[2]), id(wilber[2]))

    def test_deep_copy(self):
        will = ["Will", 28, ["Python", "C#", "JavaScript"]]
        wilber = copy.deepcopy(will)  # different object
        print_object(will, 'will info:')
        print_object(wilber, 'wilber info:')

        self.assertEqual(will, wilber)
        self.assertNotEqual(id(will), id(wilber))
        self.assertEqual(id(will[0]), id(wilber[0]))
        self.assertEqual(id(will[1]), id(wilber[1]))
        self.assertNotEqual(id(will[2]), id(wilber[2]))

        print('#' * 20)

        will[0] = "Wilber"
        will[1] = 30
        will[2].append("CSS")
        print_object(will, 'will info:')
        print_object(wilber, 'wilber info:')

        self.assertNotEqual(will, wilber)
        self.assertNotEqual(id(will), id(wilber))
        self.assertNotEqual(id(will[0]), id(wilber[0]))
        self.assertNotEqual(id(will[1]), id(wilber[1]))
        self.assertNotEqual(id(will[2]), id(wilber[2]))


if __name__ == '__main__':
    unittest.main()
