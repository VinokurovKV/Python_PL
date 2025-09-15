current_sum = 0
max_sum = -10 ** 10

while True:
    num = int(input())
    if num == 0:
        break

    current_sum += num

    if current_sum > max_sum:
        max_sum = current_sum

    if current_sum < 0:
        current_sum = 0

print(max_sum)
