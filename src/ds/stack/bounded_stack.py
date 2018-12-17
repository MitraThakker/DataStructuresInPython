from src.ds.stack import Stack


class BoundedStack(Stack):
    def __init__(self, capacity: int = 16):
        super().__init__(capacity=capacity)

    def push(self, item):
        return super().push(item)

    def pop(self):
        return super().pop()

    def top(self) -> int:
        return super().top()

    def __str__(self):
        return super().__str__()

    def __contains__(self, item):
        return super().__contains__(item)
