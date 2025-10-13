def pastri(n, filler):
  triangle = []
  for i in range(n):
    row = [1]
    if i > 0:
      for j in range(1, i):
        row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
      row.append(1)
    triangle.append(row)

  lines = []
  for row in triangle:
    lines.append(filler.join(map(str, row)))
  
  max_len = len(lines[-1])
  res = []
  for line in lines:
    current_len = len(line)
    diff = max_len - current_len

    if diff % 2 == 0:
      padding = filler * (diff // 2)
      centered = padding + line + padding
    else:
      left_padding = filler * (diff // 2)
      right_padding = filler * (diff // 2 + 1)
      centered = left_padding + line + right_padding

    res.append(centered)

  return '\n'.join(res)
