p = eval(input())
q = list(eval(input()))

if isinstance(p, int):
    p = [p]
else:
    p = list(p)

if not p:
    print("YES")
    exit()

if len(p) == 1:
    if p[0] in q:
        print("YES")
    else:
        print("NO")
    exit()

zero_p, first_p = -1, -1
for i in range(len(q)):
    if p[0] == q[i]:
        zero_p = i
        break

for i in range(zero_p + 1, len(q)):
    if q[i] == p[1]:
        first_p = i
        break

if first_p == -1:
    print("NO")
    exit()

step = first_p - zero_p

index = zero_p
for elem in p:
    if index >= len(q) or q[index] != elem:
        print("NO")
        break
    index += step
else:
    print("YES")