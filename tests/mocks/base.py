class BaseMock:
    status_code: int
    to_call: str

    def __init__(self, method: str = '', status_code: int = 200):
        self.to_call = method
        self.status_code = status_code

    def json(self):
        if self.to_call != '':
            return getattr(self, self.to_call)()
        return {
            'data': {}
        }
