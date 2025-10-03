n = int(input())
 
x = int(n ** 0.5 / 4)
while x * x <= n:
  y = int((n - x * x) ** 0.5 / 3)
  while y <= x and x * x + y * y <= n:
    z = int((n - x * x - y * y) ** 0.5 / 2)
    while z <= y and x * x + y * y + z * z <= n:
      if n - x * x - y * y - z * z <= z * z:
        t = int((n - x * x - y * y - z * z) ** 0.5)
        if x * x + y * y + z * z + t * t == n:
          print(x, y, z, t)
      z += 1
    y += 1
  x += 1