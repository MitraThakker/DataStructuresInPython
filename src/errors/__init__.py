class UnimplementedABCMethod(NotImplementedError):
    def __init__(self, message: str = ''):
        if not message:
            message = 'Abstract Base Class method invoked.'
        super().__init__(message)
