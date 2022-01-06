class Result:
    def __init__(self, message, value=None):
        self.ifsuccess = None
        self.message: str = message
        self.value: float = value

    def is_ok(self):
        return self.ifsuccess


class Ok(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.ifsuccess = True


class Error(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.ifsuccess = False
