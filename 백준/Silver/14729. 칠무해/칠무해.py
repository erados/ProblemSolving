from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

N = int(input())
q = [-100] * 7
for _ in range(N):
    a = float(input())
    if -q[0] > a:
        heappop(q)
        heappush(q, -a)

q.sort(reverse=True)
for n in q:
    print("{:.3f}".format(-n))
