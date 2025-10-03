def pattsort(pattern, seq):
  if len(pattern) != len(seq):
    print("Wrong lengths!")
    return
  
  pattern_positions = sorted(range(len(pattern)), key=lambda i: pattern[i])
  sorted_seq = sorted(seq)
  res = [0] * len(seq)
  for i, pos in enumerate(pattern_positions):
    res[pos] = sorted_seq[i]

  return res
