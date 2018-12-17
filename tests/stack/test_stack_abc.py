import unittest
from src.errors import UnimplementedABCMethod
from src.stack.stack_abc import Stack


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        Stack.__abstractmethods__ = None
        self.stack = Stack()

    def tearDown(self):
        self.stack = None

    def test_push(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.stack.push(1)

    def test_pop(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.stack.pop()

    def test_element_exists(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.stack.exists(1)

    def test_top(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.stack.top()

    def test_stringify(self):
        with self.assertRaises(UnimplementedABCMethod):
            str(self.stack)


if __name__ == '__main__':
    unittest.main()
