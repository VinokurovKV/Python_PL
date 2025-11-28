class GenerationDescriptor:
    _count = 0

    def __get__(self, instance, owner):
        return self._count

    def __set__(self, instance, value):
        raise AttributeError

    def __delete__(self, instance):
        raise AttributeError

    @classmethod
    def increment(cls):
        cls._count += 1

class Generative(type):
    def __new__(cls, name, bases, namespace):
        namespace['generation'] = GenerationDescriptor()
        new_class = super().__new__(cls, name, bases, namespace)
        GenerationDescriptor.increment()
        return new_class

    def __setattr__(cls, name, value):
        if name == 'generation':
            raise AttributeError
        super().__setattr__(name, value)

    def __delattr__(cls, name):
        if name == 'generation':
            raise AttributeError
        super().__delattr__(name)

