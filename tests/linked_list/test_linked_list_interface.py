import unittest
from src.linked_list.linked_list_interface import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        LinkedList.__abstractmethods__ = frozenset()
        self.linked_list = LinkedList()

    def tearDown(self):
        self.linked_list = None

    def test_append(self):
        self.linked_list.append(1)

    def test_prepend(self):
        self.linked_list.prepend(1)

    def test_remove(self):
        self.linked_list.remove(1)

    def test_remove_all(self):
        self.linked_list.remove_all(2)

    def test_element_exists(self):
        self.linked_list.exists(1)

    def test_size(self):
        self.linked_list.size()

    def test_stringify(self):
        str(self.linked_list)


if __name__ == "__main__":
    unittest.main()
