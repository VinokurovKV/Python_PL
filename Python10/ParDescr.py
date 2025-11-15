class ParDescr:
    def __init__(self, initial_value):
        self.initial_value = initial_value
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self.initial_value
        return instance.__dict__.get(self._name, self.initial_value)

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value
    
    def __delete__(self, instance):
        try:
            del instance.__dict__[self._name]
        except KeyError:
            raise KeyError(self._name)
