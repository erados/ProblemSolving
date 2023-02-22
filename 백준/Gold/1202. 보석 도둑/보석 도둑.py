from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

N, K = map(int, input().split())

main_heap = []
for n in range(N):
    m, v = map(int, input().split())
    heappush(main_heap, (m, v))

for k in range(K):
    heappush(main_heap, (int(input()), 1_000_001))

answer = 0
temp_heap = []
while main_heap:
    m, v = heappop(main_heap)

    if v != 1_000_001:
        heappush(temp_heap, (-v, m))

    elif temp_heap:
        answer += heappop(temp_heap)[0]

print(-answer)
