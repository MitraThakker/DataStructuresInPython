from abc import ABC, abstractmethod
from src.errors import UnimplementedABCMethod


class LinkedList(ABC):

    @abstractmethod
    def append(self, item):
        raise UnimplementedABCMethod

    @abstractmethod
    def prepend(self, item):
        raise UnimplementedABCMethod

    @abstractmethod
    def remove(self, item):
        raise UnimplementedABCMethod

    @abstractmethod
    def remove_all(self, item):
        raise UnimplementedABCMethod

    @abstractmethod
    def exists(self, item) -> bool:
        raise UnimplementedABCMethod

    @abstractmethod
    def __str__(self):
        raise UnimplementedABCMethod

    @abstractmethod
    def __len__(self):
        raise UnimplementedABCMethod
