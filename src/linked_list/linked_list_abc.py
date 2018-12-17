from abc import ABC
from src.errors import UnimplementedABCMethod


class LinkedList(ABC):

    def append(self, item):
        raise UnimplementedABCMethod

    def prepend(self, item):
        raise UnimplementedABCMethod

    def remove(self, item):
        raise UnimplementedABCMethod

    def remove_all(self, item):
        raise UnimplementedABCMethod

    def exists(self, item) -> bool:
        raise UnimplementedABCMethod

    def __str__(self):
        raise UnimplementedABCMethod

    def __len__(self):
        raise UnimplementedABCMethod
