from src.ds.stack import Stack
from src.errors import StackOverflow


class BoundedStack(Stack):

    def __init__(self, capacity: int = 16):
        super().__init__()
        self.__stack = list()
        self.capacity = capacity

    @property
    def stack(self):
        return self.__stack

    def push(self, item):
        if len(self.stack) == self.capacity:
            raise StackOverflow
        self.stack.append(item)
