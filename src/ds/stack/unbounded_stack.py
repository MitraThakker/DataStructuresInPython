from src.ds.stack import Stack


class UnboundedStack(Stack):

    def __init__(self):
        super().__init__()
        self.__stack = list()

    @property
    def stack(self):
        return self.__stack

    def push(self, item):
        self.stack.append(item)
