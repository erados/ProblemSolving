from sys import stdin

input = stdin.readline

N = int(input())
values = []

for _ in range(N):
    values.append(int(input()))

values.sort()

max_value = 0
for times in range(1, N + 1):
    new_value = values.pop() * times

    if max_value < new_value:
        max_value = new_value

print(max_value)
