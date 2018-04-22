from interface import implements
from src.linked_list.linked_list_interface import LinkedList


class Node:
	value = None
	next = None

	def __init__(self, value):
		self.value = value


class SinglyLinkedList(implements(LinkedList)):
	head = None
	__size = 0

	def size(self):
		return self.__size

	def append(self, item):
		if self.head is not None:
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = Node(value=item)
		else:
			self.head = Node(value=item)
		self.__size += 1

	def prepend(self, item):
		new_node = Node(value=item)
		new_node.next = self.head
		self.head = new_node
		self.__size += 1

	def remove(self, item):
		if self.head is not None:
			current = self.head
			if self.head.value == item:
				self.head = self.head.next
				self.__size -= 1
				return
			while current.next is not None:
				if current.next.value == item:
					current.next = current.next.next
					self.__size -= 1
					return
				current = current.next
			raise LookupError("Element " + str(item) + " not found.")
		else:
			raise LookupError("Can not remove from empty list.")

	def remove_all(self, item):
		if self.head is not None:
			current = Node(value=None)
			current.next = self.head
			self.head = current
			while current.next is not None:
				if current.next.value == item:
					current.next = current.next.next
					self.__size -= 1
				else:
					current = current.next
			self.head = self.head.next
		else:
			raise LookupError("Can not remove from empty list.")

	def exists(self, item):
		current = self.head
		while current is not None:
			if current.value == item:
				return True
			current = current.next
		return False

	def __str__(self):
		output_str = ""
		current = self.head
		while current is not None:
			output_str += str(current.value) + "->"
			current = current.next
		output_str += str(None)
		return output_str


if __name__ == "__main__":
	sll = SinglyLinkedList()
	print(sll, sll.size(), sll.head)
	sll.append("a")
	print(sll, sll.size(), sll.head.value)
	sll.prepend(1)
	print(sll, sll.size(), sll.head.value)
	print("Exists 1 " + str(sll.exists(1)))
	print("Exists 3 " + str(sll.exists(3)))
	print(sll, sll.size(), sll.head.value)
	sll.append("a")
	sll.prepend(4)
	print(sll, sll.size(), sll.head.value)
	sll.remove_all("a")
	print(sll, sll.size(), sll.head.value)
	sll.remove(4)
	try:
		sll.remove(4)
	except LookupError as le:
		print(le)
	sll.remove(1)
	print(sll, sll.size(), sll.head)
	try:
		sll.remove(4)
	except LookupError as le:
		print(le)
	print(sll, sll.size(), sll.head)
	try:
		sll.remove_all(4)
	except LookupError as le:
		print(le)
	print(sll, sll.size(), sll.head)