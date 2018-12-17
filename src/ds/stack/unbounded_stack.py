from src.ds.stack import Stack


class UnboundedStack(Stack):

    def __init__(self):
        super().__init__()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return super().pop()

    def top(self) -> int:
        return super().top()

    def __str__(self):
        return super().__str__()

    def __contains__(self, item):
        return super().__contains__(item)
