import unittest

from src.errors import StackUnderflow, StackOverflow
from src.stack.bounded_stack import BoundedStack


class TestUnboundedStack(unittest.TestCase):

    def setUp(self):
        self.stack = BoundedStack(capacity=2)

    def tearDown(self):
        del self.stack

    def test_push_success(self):
        self.stack.push(1)
        self.stack.push('qwerty')

        self.assertTrue(self.stack.exists(1))
        self.assertTrue(self.stack.exists('qwerty'))
        self.assertEqual(self.stack.top(), 1)

    def test_push_overflow(self):
        self.stack.push(1)
        self.stack.push('qwerty')

        with self.assertRaises(StackOverflow):
            self.stack.push(tuple())

    def test_pop_success(self):
        self.stack.push(1)
        popped = self.stack.pop()

        self.assertFalse(self.stack.exists(1))
        self.assertEqual(popped, 1)
        self.assertEqual(self.stack.top(), -1)

    def test_pop_underflow(self):
        with self.assertRaises(StackUnderflow):
            self.stack.pop()

    def test_element_exists_found(self):
        self.stack.push(1)

        self.assertTrue(self.stack.exists(1))
        self.assertEqual(self.stack.top(), 0)

    def test_element_exists_not_found(self):
        self.assertFalse(self.stack.exists(1))
        self.assertEqual(self.stack.top(), -1)

    def test_top(self):
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 0)

        self.stack.push(list())
        self.assertEqual(self.stack.top(), 1)

        self.stack.pop()
        self.assertEqual(self.stack.top(), 0)

        self.stack.pop()
        self.assertEqual(self.stack.top(), -1)

    def test_stringify(self):
        self.stack.push(1)
        self.stack.push('qwerty')

        self.assertIsNotNone(str(self.stack))


if __name__ == '__main__':
    unittest.main()
