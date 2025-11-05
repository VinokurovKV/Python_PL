class Dots:
  def __init__(self, start, end):
    self.start = float(start)
    self.end = float(end)

  def __getitem__(self, item):
    if type(item) == int:
      n = item
      if n <= 1:
        return iter([self.start])
      
      return (self.start + i * (self.end - self.start) / (n - 1) for i in range(n))
    elif type(item) == slice:
      i = item.start
      j = item.stop
      n = item.step

      if n is None:
        if i is None:
          i = 0
        if j <= 1:
          return self.start

        return self.start + i * (self.end - self.start) / (j - 1)

      if n <= 1:
        return iter([self.start])

      if i is None:
        i = 0
      if j is None:
        j = n

      return (self.start + idx * (self.end - self.start) / (n - 1) for idx in range(i, j))

'''a = Dots(-1,1)
print(*a[7])
print(a[0:7])
print(a[2:7])
print(a[4:7])
print(a[7:7])
print(a[-7:7])
print(*a[1:3:7])
print(*a[:3:7])
print(*a[2::7])
print(*a[::7])
print(*a[-2:8:7])'''