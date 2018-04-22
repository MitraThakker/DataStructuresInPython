import unittest
from src.linked_list.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

	def setUp(self):
		self.sll = SinglyLinkedList()

	def tearDown(self):
		self.sll = None

	def test_append_success(self):
		self.sll.append(1)
		self.sll.append(2)
		self.sll.append(3)

		self.assertEqual(self.sll.size(), 3)

	def test_prepend_success(self):
		self.sll.prepend(1)
		self.sll.prepend(2)
		self.sll.prepend(3)

		self.assertEqual(self.sll.size(), 3)

	def test_remove_head_success(self):
		self.sll.prepend(1)
		self.sll.remove(1)

		self.assertFalse(self.sll.exists(1))
		self.assertEqual(self.sll.size(), 0)

	def test_remove_mid_element_success(self):
		self.sll.append(1)
		self.sll.append(2)
		self.sll.append(3)
		self.sll.append(4)
		self.sll.remove(3)

		self.assertFalse(self.sll.exists(3))
		self.assertEqual(self.sll.size(), 3)

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

		self.assertFalse(self.sll.exists(2))
		self.assertEqual(self.sll.size(), 1)

	def test_remove_all_empty_list_failure(self):
		with self.assertRaises(LookupError):
			self.sll.remove_all(3)

	def test_element_exists_true(self):
		self.sll.append(1)
		self.sll.append(2)
		self.sll.append(3)

		self.assertTrue(self.sll.exists(3))

	def test_element_exists_false(self):
		self.sll.append(1)
		self.sll.append(2)
		self.sll.append(3)

		self.assertFalse(self.sll.exists(4))

	def test_stringify(self):
		self.sll.append(1)
		self.sll.append(2)
		self.sll.append(3)

		sll_string = str(self.sll)

		self.assertIsNot(sll_string, str(None))


if __name__ == "__main__":
	unittest.main()
