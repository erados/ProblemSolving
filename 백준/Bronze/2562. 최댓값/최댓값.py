from sys import stdin

input = stdin.readline

max = 0
i_max = -1
for i in range(1, 10):
    num = int(input())
    if num > max:
        max = num
        i_max = i

print(max)
print(i_max)
