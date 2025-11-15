class Sequence:
    _Nothing = object()
    def __init__(self, value=_Nothing):
        if value is self._Nothing:
            self._sequence = []
        else:
            self.sequence = value

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if hasattr(value, '__getitem__'):
            self._sequence = value
        else:
            self._sequence = [value]

    @sequence.deleter
    def sequence(self):
        self._sequence = type(self._sequence)()
