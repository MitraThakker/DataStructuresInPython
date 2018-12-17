from abc import ABC, abstractmethod
from src.errors import UnimplementedABCMethod


class Stack(ABC):

    @abstractmethod
    def push(self, item):
        raise UnimplementedABCMethod

    @abstractmethod
    def pop(self):
        raise UnimplementedABCMethod

    @abstractmethod
    def exists(self, item) -> bool:
        raise UnimplementedABCMethod

    @abstractmethod
    def top(self) -> int:
        raise UnimplementedABCMethod

    @abstractmethod
    def __str__(self):
        raise UnimplementedABCMethod
