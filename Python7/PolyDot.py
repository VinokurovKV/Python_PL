from itertools import starmap, islice, chain, pairwise, tee
from math import dist, atan2, pi, degrees

def perimeter(dots):
  dots_list = list(dots)
  pairs = pairwise(chain(dots_list, [dots_list[0]]))
  return sum(starmap(dist, pairs))

def convex(dots):
  dots_list = list(dots)
  n = len(dots_list)
  if n < 3:
    return True

  signs = set()
  for i in range(n):
    a, b, c = dots_list[i], dots_list[(i + 1) % n], dots_list[(i + 2) % n]
    cp = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if cp > 0:
      signs.add(1)
    else:
      signs.add(-1)
  
  return len(signs) <= 1

def inside(dot, dots):
  dots_list = list(dots)
  n = len(dots_list)

  angles = 0
  for i in range(n):
    a, b, c = dot, dots_list[i], dots_list[(i + 1) % n]

    x1 = (b[0] - a[0], b[1] - a[1])
    x2 = (c[0] - a[0], c[1] - a[1])

    x1_angle = atan2(x1[1], x1[0])
    x2_angle = atan2(x2[1], x2[0])

    angle = x2_angle - x1_angle
    if angle > pi:
      angle -= 2 * pi
    elif angle < -pi:
      angle += 2 * pi

    angles += angle
  return abs(angles) > pi

def info(dots, dot):
  d1, d2, d3 = tee(dots, 3)
  return perimeter(d1), convex(d2), inside(dot, d3)

'''
tri = (0, 0), (0, 4), (3, 0)
dot, dot2, odot, odot2 = (1, 1), (1, 2), (4, 4), (-1, -1)
print("{:.2f} {} {}".format(*info(tri, dot)))
print("{:.2f} {} {}".format(*info(tri, odot)))
print("{:.2f} {} {}".format(*iter(info(tri + (odot,), dot2))))
print("{:.2f} {} {}".format(*info(tri + (odot,), odot2)))
'''