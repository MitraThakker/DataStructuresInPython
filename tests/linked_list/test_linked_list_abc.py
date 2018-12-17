import unittest
from src.errors import UnimplementedABCMethod
from src.linked_list.linked_list_abc import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        LinkedList.__abstractmethods__ = None
        self.linked_list = LinkedList()

    def tearDown(self):
        del self.linked_list

    def test_append(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.linked_list.append(1)

    def test_prepend(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.linked_list.prepend(1)

    def test_remove(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.linked_list.remove(1)

    def test_remove_all(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.linked_list.remove_all(2)

    def test_element_exists(self):
        with self.assertRaises(UnimplementedABCMethod):
            self.linked_list.exists(1)

    def test_len(self):
        with self.assertRaises(UnimplementedABCMethod):
            len(self.linked_list)

    def test_stringify(self):
        with self.assertRaises(UnimplementedABCMethod):
            str(self.linked_list)


if __name__ == '__main__':
    unittest.main()
