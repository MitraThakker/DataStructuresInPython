from abc import ABC, abstractmethod


class LinkedList(ABC):

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def append(self, item):
        pass

    @abstractmethod
    def prepend(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def remove_all(self, item):
        pass

    @abstractmethod
    def exists(self, item):
        pass

    @abstractmethod
    def __str__(self):
        return ""
