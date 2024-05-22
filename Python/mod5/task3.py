class BlockErrors:
    def __init__(self, errorsType):
        self.errorsType=errorsType
    def __enter__(self):
        pass
    def __exit__(self, type, value, traceback):
        if type is not None and issubclass(type, self.errorsType):
            return True

err=(ZeroDivisionError, TypeError)

with BlockErrors(err):
    a = 1 / 0
print('Выполнено без ошибок')
