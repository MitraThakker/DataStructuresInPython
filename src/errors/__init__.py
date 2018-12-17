class UnimplementedABCMethod(NotImplementedError):
    def __init__(self, message: str = ''):
        if not message:
            message = 'Abstract Base Class method invoked.'
        super().__init__(message)


class StackUnderflow(RuntimeError):
    def __init__(self, message: str = ''):
        if not message:
            message = 'Can\'t perform pop(). Stack is already empty.'
        super().__init__(message)


class StackOverflow(RuntimeError):
    def __init__(self, message: str = ''):
        if not message:
            message = 'Can\'t perform push(). Stack is already full.'
        super().__init__(message)


class QueueUnderflow(RuntimeError):
    def __init__(self, message: str = ''):
        if not message:
            message = 'Can\'t perform dequeue(). Queue is already empty.'
        super().__init__(message)


class QueueOverflow(RuntimeError):
    def __init__(self, message: str = ''):
        if not message:
            message = 'Can\'t perform enqueue(). Queue is already full.'
        super().__init__(message)
