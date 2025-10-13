lines = []
while (s := input()):
  lines.append(s)

rectangles = []
for line in lines:
  parts = line.split()
  x, y, w, h = map(int, parts[:4])
  char = parts[4]

  if not w or not h:
    continue

  x1 = x if w > 0 else x + w
  x2 = x + w if w > 0 else x
  y1 = y if h > 0 else y + h
  y2 = y + h if h > 0 else y

  rectangles.append((x1, y1, x2, y2, char))  

min_x = min(r[0] for r in rectangles)
max_x = max(r[2] for r in rectangles)
min_y = min(r[1] for r in rectangles)
max_y = max(r[3] for r in rectangles)
  
width = max_x - min_x
height = max_y - min_y

screen = [['.'] * width for _ in range(height)]

for x1, y1, x2, y2, char in rectangles:
  for i in range(y1, y2):
    row = screen[i - min_y]
    for j in range(x1, x2):
      row[j - min_x] = char

for row in screen:
  print(''.join(row))
