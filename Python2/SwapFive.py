'''
n = ABCDEk
n * k = kABCDE
ABCDE == (n - k) // 10
kABCDE == (n - k) // 10 + k * P
n * k = (n - k) // 10 + k * P
'''

k = int(input())

if k == 0:
    print(0)
elif k == 1:
    print(1)
else:
    m = 1
    while True:
        P = 10 ** m
        a = k * (10 * P - 1)
        b = 10 * k - 1

        if a % b == 0:
            n = a // b
            if n % 10 == k:
                print(n)
                break
        m += 1
