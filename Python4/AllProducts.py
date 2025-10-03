def rec_dels(x, start=2, dels=None):
  if dels is None:
    dels = []

  if x == 1:
    if len(dels) != 0:
      print(*dels, sep="*")
    return
  
  for d in range(start, int(x**0.5) + 1):
    if x % d == 0:
      rec_dels(x // d, d, dels + [d])

  if len(dels) == 0 or x >= dels[-1]:
    print(*dels + [x], sep="*")

x = int(input())
rec_dels(x)