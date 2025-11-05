import itertools

def manyfor(order, *sequences):
  iterators = [iter(seq) for seq in sequences]

  if isinstance(order, (list, tuple)):
    order_i = itertools.cycle(order)
  else:
    order_i = iter(order)

  while True:
    try:
      i = next(order_i)
    except StopIteration:
      return
    
    if i < 0 or i >= len(iterators):
      return
    
    try:
      yield next(iterators[i])
    except StopIteration:
      return

'''
from itertools import cycle, repeat, takewhile, count
N = 300000
print(sum(manyfor(map(lambda x: x % 3, takewhile(lambda x: x < N, count())), cycle(range(4)), repeat(1), count())))
'''