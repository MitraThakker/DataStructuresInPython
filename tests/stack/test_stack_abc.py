import unittest
from src.errors import UnimplementedABCMethod
from src.ds.stack import Stack


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        Stack.__abstractmethods__ = None
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_property_stack(self):
        self.assertIsNotNone(self.stack.stack)

    def test_push(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.stack.push(1)


if __name__ == '__main__':
    unittest.main()
