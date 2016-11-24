from __future__ import print_function
import unittest
import contextlib
import os
import os.path


@contextlib.contextmanager
def change_cwd(directory):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    new_dir = os.path.join(current_dir, directory)
    old_cwd = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(old_cwd)


class ContextTestCase(unittest.TestCase):
    def test_contextmanager(self):
        cwd = os.getcwd()
        print(cwd)

        with change_cwd('..'):
            new_cwd = os.getcwd()
            self.assertNotEqual(cwd, new_cwd)
            print(new_cwd)

        new_cwd = os.getcwd()
        self.assertEqual(cwd, new_cwd)
        print(new_cwd)


if __name__ == '__main__':
    unittest.main()
