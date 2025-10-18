import re

def evalform(formula, *args):
    variables = sorted(set(re.findall(r'[a-zA-Z]+', formula)))
    
    namespace = {}
    for var, value in zip(variables, args):
        namespace[var] = value
  
    return eval(formula, namespace)
