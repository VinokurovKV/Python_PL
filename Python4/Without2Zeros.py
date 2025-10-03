def No_2Zero(N, K):
  if N == 1:
    return K - 1
  zero_end = K - 1
  not_zero_end = (K - 1) * (K - 1)
  for i in range(3, N + 1):
    new_zero_end = not_zero_end
    new_not_zero_end = (zero_end + not_zero_end) * (K - 1)
    zero_end = new_zero_end
    not_zero_end = new_not_zero_end

  return zero_end + not_zero_end
