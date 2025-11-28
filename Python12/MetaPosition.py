class positioned(type):
    def __new__(cls, name, bases, namespace):
        annotations = namespace.get('__annotations__', {})
        new_class = super().__new__(cls, name, bases, namespace)

        field_order = tuple(annotations.keys())
        new_class.__match_args__ = field_order

        def __init__(self, *args):
            for i, field in enumerate(field_order):
                if i < len(args):
                    setattr(self, field, args[i])
                elif field in namespace and not field.startswith('__'):
                    setattr(self, field, namespace[field])
                elif field in annotations:
                    raise AttributeError

        new_class.__init__ = __init__

        def __str__(self):
            fields = []
            for field in field_order:
                if hasattr(self, field):
                    fields.append(f"{field}={getattr(self, field)}")
            return " ".join(fields)

        new_class.__str__ = __str__

        return new_class
