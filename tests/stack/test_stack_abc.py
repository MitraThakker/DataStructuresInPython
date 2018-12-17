import unittest
from src.errors import UnimplementedABCMethod, StackUnderflow
from src.ds.stack import Stack


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        Stack.__abstractmethods__ = None
        self.stack = Stack()

    def tearDown(self):
        self.stack = None

    def test_push(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.stack.push(1)


if __name__ == '__main__':
    unittest.main()
