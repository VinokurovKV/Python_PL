state, n, a, b = eval(input())

bit_mask = (1 << 64) - 1

for _ in range(n):
    state ^= state << 7
    state &= bit_mask

    state ^= state >> 9
    state &= bit_mask

shift_range = b - a + 1
pseudo_random = a + (state % shift_range)

print(pseudo_random)
