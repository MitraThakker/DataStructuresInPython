from src.errors import StackUnderflow, StackOverflow
from src.stack.stack_abc import Stack


class BoundedStack(Stack):

    def __init__(self, capacity: int = 16):
        self.__stack = list()
        self.capacity = capacity

    @property
    def stack(self):
        return self.__stack

    def push(self, item):
        if len(self.stack) == self.capacity:
            raise StackOverflow
        self.stack.append(item)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise StackUnderflow

    def exists(self, item) -> bool:
        return item in self.stack

    def top(self) -> int:
        return len(self.stack) - 1

    def __str__(self):
        output_str = '\n'
        stringified_list = list(map(str, self.stack))
        max_width = max([len(i) for i in stringified_list])
        for i in reversed(self.stack):
            item_repr = f'{i}'.ljust(max_width)
            output_str += f'| {item_repr} |\n'
        output_str += f' _{"_" * max_width}_\n'
        return output_str
