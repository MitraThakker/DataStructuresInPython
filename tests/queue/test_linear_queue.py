import unittest

from src.ds.queue import LinearQueue
from src.errors import QueueOverflow, QueueUnderflow


class TestLinearQueue(unittest.TestCase):

    def setUp(self):
        self.q = LinearQueue(capacity=2)

    def tearDown(self):
        del self.q

    def test_enqueue_success(self):
        self.q.enqueue(1)
        self.q.enqueue('qwerty')

        self.assertFalse(self.q.is_empty())
        self.assertTrue(self.q.is_full())
        self.assertEqual(len(self.q), 2)

    def test_enqueue_overflow(self):
        self.q.enqueue(1)
        self.q.enqueue('qwerty')

        with self.assertRaises(QueueOverflow):
            self.q.enqueue('1337')

    def test_dequeue_success(self):
        self.q.enqueue(1)
        self.q.enqueue('qwerty')
        self.q.dequeue()
        self.q.dequeue()

        self.assertTrue(self.q.is_empty())
        self.assertFalse(self.q.is_full())
        self.assertEqual(len(self.q), 0)

    def test_dequeue_underflow(self):
        with self.assertRaises(QueueUnderflow):
            self.q.dequeue()

    def test_peek_success(self):
        self.q.enqueue(1)
        self.q.enqueue('qwerty')

        self.assertEqual(self.q.peek(), 1)
        self.assertEqual(len(self.q), 2)

    def test_peek_underflow(self):
        with self.assertRaises(QueueUnderflow):
            self.q.peek()

    def test_is_full(self):
        self.q.enqueue(1)
        self.q.enqueue('qwerty')

        self.assertTrue(self.q.is_full())

    def test_is_empty(self):
        self.assertTrue(self.q.is_empty())

    def test_stringify(self):
        self.q.enqueue(1)
        self.assertIsNotNone(str(self.q))

    def test_len(self):
        self.assertEqual(len(self.q), 0)

    def test_contains_true(self):
        self.q.enqueue(1)
        self.assertTrue(1 in self.q)

    def test_contains_false(self):
        self.assertFalse(1 in self.q)


if __name__ == '__main__':
    unittest.main()
