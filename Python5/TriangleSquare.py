from decimal import *

getcontext().prec = 200

sides = input().strip().split(',')
x1, y1, x2, y2, x3, y3 = map(Decimal, sides)

#print(abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / Decimal(2))
print(abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / Decimal(2))
