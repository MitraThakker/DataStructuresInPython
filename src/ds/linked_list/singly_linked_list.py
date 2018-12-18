from src.ds.linked_list import LinkedList


class Node:
    value = None
    next = None

    def __init__(self, value):
        self.value = value


class SinglyLinkedList(LinkedList):
    head = None
    __size = 0

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
            raise LookupError(f'Element {item} not found.')
        else:
            raise LookupError('Can not remove from empty list.')

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
            raise LookupError('Can not remove from empty list.')

    def __contains__(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False

    def __str__(self):
        output_str = ''
        current = self.head
        while current is not None:
            output_str += str(current.value) + '->'
            current = current.next
        output_str += str(None)
        return output_str

    def __len__(self):
        return self.__size
