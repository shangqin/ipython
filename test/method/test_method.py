from __future__ import print_function
import unittest

"""
http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

1, @staticmethod
    Convert a function to be a static method.

    A static method does not receive an implicit first argument.
    To declare a static method, use this idiom:

         class C:
         def f(arg1, arg2, ...): ...
         f = staticmethod(f)

    It can be called either on the class (e.g. C.f()) or on an instance
    (e.g. C().f()).  The instance is ignored except for its class.

2, @classmethod
    Convert a function to be a class method.

    A class method receives the class as implicit first argument,
    just like an instance method receives the instance.
    To declare a class method, use this idiom:

      class C:
          def f(cls, arg1, arg2, ...): ...
          f = classmethod(f)

    It can be called either on the class (e.g. C.f()) or on an instance
    (e.g. C().f()).  The instance is ignored except for its class.
    If a class method is called for a derived class, the derived class
    object is passed as the implied first argument.
"""


class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


class MethodTestCase(unittest.TestCase):
    def test_method(self):
        a = A()

        # 1, a.foo is bound method
        print('1, normal method, or instance method')
        print(a.foo)  # bound method, partial function, expect 1 argument, instance a is bound to foo
        print(A.foo)  # unbound method, expect 2 arguments
        a.foo(1)
        A.foo(a, 1)

        # 2, class method
        print('2, class method')
        print(a.class_foo)  # bound method
        print(A.class_foo)  # bound method, class A is bound to class_foo
        a.class_foo(1)
        A.class_foo(1)

        # 3, static method
        print('3, static method')
        print(a.static_foo)  # function
        print(A.static_foo)  # function
        a.static_foo(1)
        A.static_foo(1)


if __name__ == '__main__':
    unittest.main()
