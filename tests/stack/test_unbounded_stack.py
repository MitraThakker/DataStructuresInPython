import unittest

from src.ds.stack import UnboundedStack


class TestUnboundedStack(unittest.TestCase):

    def setUp(self):
        self.stack = UnboundedStack()

    def tearDown(self):
        del self.stack

    def test_push(self):
        self.stack.push(1)
        self.stack.push('qwerty')
        self.stack.push('1337')

        self.assertTrue(1 in self.stack)
        self.assertTrue('qwerty' in self.stack)
        self.assertTrue('1337' in self.stack)
        self.assertEqual(self.stack.top(), 2)

    def test_pop(self):
        self.stack.push(1)
        popped = self.stack.pop()

        self.assertEqual(popped, 1)
        self.assertEqual(self.stack.top(), -1)
        self.assertTrue(1 not in self.stack)

    def test_stringify(self):
        self.stack.push(1)
        self.assertIsNotNone(str(self.stack))


if __name__ == '__main__':
    unittest.main()
