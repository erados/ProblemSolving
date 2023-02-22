from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

N, K = map(int, input().split())

jewels = []
for n in range(N):
    m, v = map(int, input().split())
    jewels.append((v, m))
jewels.sort(key=lambda x: x[1])

bags = []
for k in range(K):
    bags.append(int(input()))
bags.sort()

answer = 0
heap = []
jewel_idx = 0
for bag in bags:
    while jewel_idx < len(jewels) and jewels[jewel_idx][1] <= bag:
        heappush(heap, -jewels[jewel_idx][0])
        jewel_idx += 1

    if heap:
        answer += heappop(heap)

print(-answer)
