from string import ascii_lowercase
from itertools import product, islice

def slotgen(number):
    def decorator(cls):
        original_attrs = {
            name: value
            for name, value in vars(cls).items()
            if not name.startswith('__')
        }
        
        length = 1
        while len(ascii_lowercase) ** length < number:
            length += 1
        
        slot_names = []
        for name_tuple in islice(product(ascii_lowercase, repeat=length), number):
            slot_names.append(''.join(name_tuple))
        
        class_dict = {
            '__slots__': slot_names,
            '__module__': cls.__module__,
            '__doc__': cls.__doc__
        }
        
        for attr_name, attr_value in original_attrs.items():
            if attr_name not in slot_names:
                class_dict[attr_name] = attr_value
        
        NewClass = type(cls.__name__, (object,), class_dict)
        
        original_setattr = NewClass.__setattr__
        
        def __setattr__(self, name, value):
            if name not in self.__slots__ and hasattr(type(self), name):
                raise AttributeError(f"'{self.__class__.__name__}' object attribute '{name}' is read-only")
            original_setattr(self, name, value)
        
        NewClass.__setattr__ = __setattr__
        
        return NewClass
    
    return decorator
