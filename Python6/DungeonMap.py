graph = {}
while True:
  s = input()
  if ' ' not in s:
    start = s
    break
  a, b = s.split()
  graph.setdefault(a, set()).add(b)
  graph.setdefault(b, set()).add(a)

end = input()

visited = {start}
queue = [start]
while queue:
  current = queue.pop(0)
  if current == end:
    print("YES")
    break
  for neighbor in graph.get(current, []):
    if neighbor not in visited:
      visited.add(neighbor)
      queue.append(neighbor)
else:
    print("NO")