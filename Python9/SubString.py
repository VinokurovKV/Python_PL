class SubString(__import__('collections').UserString):
    def __sub__(self, other):
        from collections import Counter
        if isinstance(other, SubString):
            other_str = other.data
        else: 
            other_str = other
        
        other_list = Counter(other_str)
        result = []

        for c in self.data:
            if other_list[c] > 0:
                other_list[c] -= 1
            else:
                result.append(c)

        return SubString(''.join(result))
