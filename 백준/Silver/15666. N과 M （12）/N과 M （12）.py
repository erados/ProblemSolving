from sys import stdin
from itertools import combinations_with_replacement
from collections import defaultdict

input = stdin.readline

N, M = map(int, input().split())

nums = sorted(list(set(map(int, input().split()))))

visited = defaultdict(bool)

for comb in combinations_with_replacement(nums, M):
    if not visited[comb]:
        visited[comb]
        print(*comb)
