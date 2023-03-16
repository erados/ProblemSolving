from sys import stdin
from math import isqrt

input = stdin.readline
T = int(input())


def solve():
    n = int(input())
    left = 1
    right = 141421356
    while left + 1 < right:
        mid = (left + right) // 2
        if mid * (mid + 1) / 2 <= n:
            left = mid
        else:
            right = mid

    return left


for _ in range(T):
    print(solve())
