from sys import stdin
from itertools import combinations
from collections import Counter
from bisect import bisect_left

input = stdin.readline

N, S = map(int, input().split())
nums = [*map(int, input().split())]

A = nums[: N // 2]
B = nums[N // 2 :]

B_sum_comb = []

for i in range(len(B) + 1):
    for comb in combinations(B, i):
        B_sum_comb.append(sum(comb))

counter = Counter(B_sum_comb)
counter_keys = sorted(counter.keys())

answer = 0
for i in range(len(A) + 1):
    for comb in combinations(A, i):
        num_need = S - sum(comb)
        idx = bisect_left(counter_keys, num_need)

        if idx < len(counter_keys) and counter_keys[idx] == num_need:
            answer += counter[num_need]

print(answer if S else answer - 1)
