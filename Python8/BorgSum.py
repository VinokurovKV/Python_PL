class Borg:
  values = []
  active_props = []

  def __init__(self, value=0):
    self.index = len(Borg.values)

    Borg.values.append(value)
    Borg.active_props.append(True)

  def __str__(self):
    return str(Borg.values[self.index])
  
  def __iter__(self):
    return iter(Borg.values[i] for i in range(len(Borg.values)) if Borg.active_props[i])
  
  def __iadd__(self, other):
    for i in range(len(Borg.values)):
      if Borg.active_props[i]:
        Borg.values[i] += other
    
    return self
  
  def __isub__(self, other):
    for i in range(len(Borg.values)):
      if Borg.active_props[i]:
        Borg.values[i] -= other
    
    return self
  
  def __del__(self):
    Borg.active_props[self.index] = False

'''a, b, c = Borg(5), Borg(10), Borg(16)
print(a, b, c)
print(*a)
b += 10
c -= 1
print(*a)
del b
print(*a) '''