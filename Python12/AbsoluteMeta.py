from collections.abc import Callable
from inspect import getfullargspec

class AbsDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__abs__()

class Absolute(type):
    def __new__(cls, name, bases, namespace, /, width="width", height="height"):
        original_abs = namespace.get("abs", None)
        
        existing_abs = namespace.get("__abs__", None)
        if existing_abs is not None and isinstance(existing_abs, Callable):
            pass
        else:
            need_to_create_abs = True
            
            if "abs" in namespace and isinstance(namespace["abs"], Callable):
                abs_method = namespace["abs"]
                try:
                    argspec = getfullargspec(abs_method)
                    if len(argspec.args) <= 1 and not argspec.varargs and not argspec.varkw:
                        namespace["_original_abs"] = abs_method
                        def __abs__(self):
                            return self._original_abs()
                        namespace["__abs__"] = __abs__
                        need_to_create_abs = False
                except:
                    pass
            
            if need_to_create_abs and "__len__" in namespace and isinstance(namespace["__len__"], Callable):
                len_method = namespace["__len__"]
                try:
                    argspec = getfullargspec(len_method)
                    if len(argspec.args) <= 1 and not argspec.varargs and not argspec.varkw:
                        def __abs__(self):
                            return self.__len__()
                        namespace["__abs__"] = __abs__
                        need_to_create_abs = False
                except:
                    pass
            
            if need_to_create_abs and (width in namespace and isinstance(namespace[width], Callable) and
                  height in namespace and isinstance(namespace[height], Callable)):
                width_method = namespace[width]
                height_method = namespace[height]
                try:
                    argspec_width = getfullargspec(width_method)
                    argspec_height = getfullargspec(height_method)
                    
                    if (len(argspec_width.args) <= 1 and not argspec_width.varargs and not argspec_width.varkw and
                        len(argspec_height.args) <= 1 and not argspec_height.varargs and not argspec_height.varkw):
                        def __abs__(self):
                            return getattr(self, width)() * getattr(self, height)()
                        namespace["__abs__"] = __abs__
                        need_to_create_abs = False
                except:
                    pass
            
            if need_to_create_abs:
                has_width_field = width in namespace and not isinstance(namespace[width], Callable)
                has_height_field = height in namespace and not isinstance(namespace[height], Callable)
                
                for base in bases:
                    if hasattr(base, width) and not isinstance(getattr(base, width, None), Callable):
                        has_width_field = True
                    if hasattr(base, height) and not isinstance(getattr(base, height, None), Callable):
                        has_height_field = True
                
                if has_width_field and has_height_field:
                    def __abs__(self):
                        return getattr(self, width) * getattr(self, height)
                    namespace["__abs__"] = __abs__
                    need_to_create_abs = False
            
            if need_to_create_abs:
                def __abs__(self):
                    return self
                namespace["__abs__"] = __abs__
        
        namespace["abs"] = AbsDescriptor()
        
        return super().__new__(cls, name, bases, namespace)
