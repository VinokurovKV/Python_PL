lst = []
while s := input():
    s = eval(s)
    if type(s) == int:
      s = [s]
    else:
      s = list(s)
    lst.append(s)
n = len(lst)

result = [[0] * (i + 1) for i in range(n)]
for i in range(n):
    for j in range(i + 1):
        result[n - 1 - j][i - j] = lst[i][j]

for i in range(n):
    print(*result[i], sep=", ")