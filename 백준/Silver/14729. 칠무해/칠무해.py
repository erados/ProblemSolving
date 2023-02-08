from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

N = int(input())
q = []
for _ in range(N):
    heappush(q, float(input()))

for _ in range(7):
    print("{:.3f}".format(heappop(q)))
