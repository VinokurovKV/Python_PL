class Defaulter:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for name, type_ in cls.__annotations__.items():
            if isinstance(type_, type):
                setattr(cls, name, type_())

'''class C(Defaulter):
    A: int 
    B: float = 123.456
    C: "Not a type" # type: ignore

a = C() 
print(C.A, C.B, hasattr(C, "C"), a.A, a.B, hasattr(a, "C"))'''
