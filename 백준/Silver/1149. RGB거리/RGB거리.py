from sys import stdin

input = stdin.readline

N = int(input())


def _min(a, b):
    return b if b < a else a


r, g, b = map(int, input().split())
for i in range(1, N):
    c_r, c_g, c_b = map(int, input().split())
    r, g, b = (
        c_r + _min(g, b),
        c_g + _min(r, b),
        c_b + _min(r, g),
    )

print(min(r, g, b))
