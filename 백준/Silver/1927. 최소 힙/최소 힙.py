from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

N = int(input())
q = []
for _ in range(N):
    a = int(input())
    if a:
        heappush(q, a)
    elif len(q) == 0:
        print(0)
    else:
        print(heappop(q))
