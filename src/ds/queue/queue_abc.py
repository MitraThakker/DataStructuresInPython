from abc import ABC, abstractmethod
from src.errors import (
    QueueOverflow,
    QueueUnderflow
)


class Queue(ABC):

    def __init__(self, capacity: int = 16):
        self.__q = list()
        self.capacity = capacity

    @property
    def q(self):
        return self.__q

    @abstractmethod
    def enqueue(self, item):
        if len(self.q) == self.capacity:
            raise QueueOverflow
        self.q.append(item)

    @abstractmethod
    def dequeue(self):
        try:
            return self.q.pop(0)
        except IndexError:
            raise QueueUnderflow

    @abstractmethod
    def peek(self):
        try:
            return self.q[0]
        except IndexError:
            raise QueueUnderflow

    @abstractmethod
    def is_full(self):
        return len(self.q) == self.capacity

    @abstractmethod
    def is_empty(self):
        return len(self.q) == 0

    @abstractmethod
    def __str__(self):
        output_str = 'F|'
        for i in self.q:
            output_str += f' {i} |'
        output_str += 'R'
        return output_str

    @abstractmethod
    def __len__(self):
        return len(self.q)

    @abstractmethod
    def __contains__(self, item):
        return item in self.q
