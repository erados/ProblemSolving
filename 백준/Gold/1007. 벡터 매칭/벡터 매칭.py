from sys import stdin, maxsize
from itertools import combinations
from math import sqrt

input = stdin.readline
T = int(input())


def solve():
    N = int(input())
    nums = []
    total_x = 0
    total_y = 0
    for n in range(N):
        x, y = map(int, input().split())
        nums.append([x, y])
        total_x += x
        total_y += y

    answer = maxsize

    for comb in combinations(nums, N // 2):
        sum_selected_x = 0
        sum_selected_y = 0
        for x, y in comb:
            sum_selected_x += x
            sum_selected_y += y

        temp = pow(total_x - 2 * sum_selected_x, 2) + pow(
            total_y - 2 * sum_selected_y, 2
        )

        if temp < answer:
            answer = temp

    print(sqrt(answer))
    return


for _ in range(T):
    solve()
