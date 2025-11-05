import math

class Triangle:
  def __init__(self, a, b, c):
    self.a = float(a)
    self.b = float(b)
    self.c = float(c)

  def __bool__(self):
    if self.a <= 0 or self.b <= 0 or self.c <= 0:
      return False
    else:
      if (self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a):
        return False
      else: 
        return True
  
  def __abs__(self):
    if not self:
      return 0.0
    
    p = (self.a + self.b + self.c) / 2
    s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    return s
  
  def __eq__(self, other):
    abc = sorted([self.a, self.b, self.c])
    a1b1c1 = sorted([other.a, other.b, other.c])

    return (math.isclose(abc[0], a1b1c1[0]) and math.isclose(abc[1], a1b1c1[1]) and math.isclose(abc[2], a1b1c1[2]))
  
  def __lt__(self, other):
    return abs(self) < abs(other)
  
  def __le__(self, other):
    return abs(self) <= abs(other)
  
  def __gt__(self, other):
    return abs(self) > abs(other)
  
  def __ge__(self, other):
    return abs(self) >= abs(other)
  
  def __str__(self):
    return f"{self.a}:{self.b}:{self.c}"
  
'''tri = Triangle(3, 4, 5), Triangle(5, 4, 3), Triangle(7, 1, 1), Triangle(5, 5, 5), Triangle(7, 4, 4)
for a, b in zip(tri[:-1], tri[1:]):
    print(a if a else b)
    print(f"{a}={abs(a):.2f} {b}={abs(b):.2f}")
    print(a == b)
    print(a >= b)
    print(a < b)'''