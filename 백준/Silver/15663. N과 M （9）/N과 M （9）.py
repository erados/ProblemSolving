from sys import stdin
from itertools import permutations
from collections import defaultdict

input = stdin.readline

N, M = map(int, input().split())

nums = sorted([*map(int, input().split())])
visited = defaultdict(bool)

for comb in permutations(nums, M):
    if not visited[comb]:
        print(*comb)
        visited[comb] = True
