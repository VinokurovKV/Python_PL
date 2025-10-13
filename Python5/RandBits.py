import random

def randbits(p, n):
  if n < 0 or n > p:
    return 0
  
  positions = random.sample(range(p), n)

  result = 0
  for pos in positions:
    result |= (1 << pos)
  return result
