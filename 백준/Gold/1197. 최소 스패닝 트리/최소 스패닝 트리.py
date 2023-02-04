from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop

input = stdin.readline

V, E = map(int, input().split())
graph = defaultdict(list)
visited = defaultdict(bool)

for _ in range(E):
    S, E, W = map(int, input().split())
    graph[S].append((W, E))
    graph[E].append((W, S))


heap = [(0, 1)]
ans = 0
while heap:
    weight, node = heappop(heap)

    if visited[node]:
        continue

    visited[node] = True
    ans += weight

    for n_node in graph[node]:
        if not visited[n_node[1]]:
            heappush(heap, n_node)
print(ans)
