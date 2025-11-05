import itertools

def LookSay():
  seq = [1]

  while True:
    for n in seq:
      yield n

    next_seq = []
    for key, group in itertools.groupby(seq):
      count = len(list(group))
      next_seq.extend([count, key])
    seq = next_seq

'''
for i, l in enumerate(LookSay()):
  print(f"{i}: {l}")
  if i > 10:
      break
'''