from src.ds.queue import Queue


class LinearQueue(Queue):
    def __init__(self, capacity: int = 16):
        super().__init__(capacity=capacity)

    def enqueue(self, item):
        return super().enqueue(item)

    def dequeue(self):
        return super().dequeue()

    def peek(self):
        return super().peek()

    def is_full(self):
        return super().is_full()

    def is_empty(self):
        return super().is_empty()

    def __str__(self):
        return super().__str__()

    def __len__(self):
        return super().__len__()

    def __contains__(self, item):
        return super().__contains__(item)
