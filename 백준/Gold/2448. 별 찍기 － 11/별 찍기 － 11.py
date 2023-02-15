from sys import stdin

input = stdin.readline

N = int(input())

unit = ["*", "* *", "*****"]
gap = 5
j = 0
for i in range(N):
    space = N - i - 1
    print(" " * space + unit[i] + " " * space)
    if gap < 0:
        gap = len(unit[-1])
        j = 0
    unit.append(unit[j] + " " * gap + unit[j])
    gap -= 2
    j += 1
