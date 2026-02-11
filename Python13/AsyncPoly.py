import asyncio
import unicodedata
import re
from typing import Optional

class YesFuture:
    def __init__(self, value: Optional[float] = None):
        self._value = value
    
    def set(self, new_value: float) -> None:
        self._value = new_value
    
    def __await__(self):
        yield
        return self._value
    
    def __repr__(self):
        return f"YesFuture({self._value})"

def parse_poly(poly: str, x: YesFuture):
    poly = poly.replace(" ", "")
    
    pattern = r'([+-]?)(\d*)(x?)([⁰¹²³⁴⁵⁶⁷⁸⁹]*)(?=[+-]|$)'
    
    terms = []
    for match in re.finditer(pattern, poly):
        if not match.group():
            continue
            
        sign = match.group(1)
        coeff = match.group(2)
        has_x = match.group(3)
        exponent_sup = match.group(4)
        
        if not any([coeff, has_x, exponent_sup]):
            continue
        
        is_positive = sign != '-'
        
        if coeff == '':
            if has_x:
                coeff_num = 1
            else:
                coeff_num = 1
        else:
            coeff_num = int(coeff)
        
        if not is_positive:
            coeff_num = -coeff_num
        
        if not has_x:
            exponent = 0
        elif exponent_sup == '':
            exponent = 1
        else:
            exponent = 0
            for char in exponent_sup:
                exponent = exponent * 10 + unicodedata.digit(char)
        
        terms.append((coeff_num, exponent))
    
    async def evaluate_poly():
        term_coroutines = []
        
        for coeff, exp in terms:
            if exp == 0:
                const_future = YesFuture(coeff)
                term_coroutines.append(const_future)
            elif coeff == 1 and exp == 1:
                term_coroutines.append(x)
            else:
                if exp == 1:
                    power_result = x
                else:
                    exp_future = YesFuture(exp)
                    power_result = Pow(x, exp_future)
                
                if coeff == 1:
                    term_coroutines.append(power_result)
                elif coeff == -1:
                    coeff_future = YesFuture(-1)
                    term_coroutines.append(Mul(coeff_future, power_result))
                else:
                    coeff_future = YesFuture(coeff)
                    term_coroutines.append(Mul(coeff_future, power_result))
        
        if not term_coroutines:
            zero_future = YesFuture(0)
            return await zero_future
        
        result = term_coroutines[0]
        
        for term in term_coroutines[1:]:
            result = Sum(result, term)
        
        return await result
    
    return evaluate_poly()

