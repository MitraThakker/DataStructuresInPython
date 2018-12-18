import unittest
from src.ds.linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.sll = SinglyLinkedList()

    def tearDown(self):
        del self.sll

    def test_append_success(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)

        self.assertEqual(len(self.sll), 3)

    def test_prepend_success(self):
        self.sll.prepend(1)
        self.sll.prepend(2)
        self.sll.prepend(3)

        self.assertEqual(len(self.sll), 3)

    def test_remove_head_success(self):
        self.sll.prepend(1)
        self.sll.remove(1)

        self.assertFalse(1 in self.sll)
        self.assertEqual(len(self.sll), 0)

    def test_remove_mid_element_success(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)
        self.sll.append(4)
        self.sll.remove(3)

        self.assertFalse(3 in self.sll)
        self.assertEqual(len(self.sll), 3)

    def test_remove_empty_list_failure(self):
        with self.assertRaises(LookupError):
            self.sll.remove(3)

    def test_remove_element_not_found_failure(self):
        self.sll.append(1)

        with self.assertRaises(LookupError):
            self.sll.remove(3)

    def test_remove_all_success(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(2)
        self.sll.remove_all(2)

        self.assertFalse(2 in self.sll)
        self.assertEqual(len(self.sll), 1)

    def test_remove_all_empty_list_failure(self):
        with self.assertRaises(LookupError):
            self.sll.remove_all(3)

    def test_contains_true(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)

        self.assertTrue(3 in self.sll)

    def test_contains_false(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)

        self.assertFalse(4 in self.sll)

    def test_stringify(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)

        self.assertIsNotNone(str(self.sll))


if __name__ == '__main__':
    unittest.main()
