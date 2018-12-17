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


if __name__ == '__main__':
    unittest.main()
