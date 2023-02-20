from sys import stdin
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

    answer = 10**7

    for comb in combinations(nums, N // 2):
        sum_selected_x = 0
        sum_selected_y = 0

        for x, y in comb:
            sum_selected_x += x
            sum_selected_y += y

        temp = sqrt(
            pow(total_x - 2 * sum_selected_x, 2) + pow(total_y - 2 * sum_selected_y, 2)
        )

        if temp < answer:
            answer = temp

    print(answer)
    return


for _ in range(T):
    solve()
