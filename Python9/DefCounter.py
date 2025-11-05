class DefCounter(__import__('collections').Counter):
    def __init__(self, iterable=None, missing=-1, **kwds):
        super().__init__(iterable, **kwds)
        self.missing = missing
    def __missing__(self, key):
        return self.missing
    def __abs__(self):
        return sum(value for value in self.values() if value > 0)
    def total(self):
        return sum(self.values())
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
    def __repr__(self):
        return f"{super().__repr__()}"
