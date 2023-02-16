from sys import stdin, maxsize
from collections import defaultdict
from heapq import heappop, heappush

input = stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)

for m in range(M):
    S, E, W = map(int, input().split())
    graph[S].append((W, E))

S, E = map(int, input().split())


def dijkstra():
    q = [(0, 0, S)]
    dist = [maxsize] * (N + 1)
    dist[S] = 0
    visited = [False] * (N + 1)
    parent = {}

    while q:
        curr_dist, last_city, curr_city = heappop(q)
        if curr_dist > dist[curr_city]:
            continue
        visited[curr_city] = True
        parent[curr_city] = last_city

        if curr_city == E:
            return (curr_dist, parent)
        for weight, new_city in graph[curr_city]:
            # if visited[new_city]:
            # continue
            new_dist = weight + curr_dist
            if dist[new_city] <= new_dist:
                continue

            dist[new_city] = new_dist
            heappush(q, (new_dist, curr_city, new_city))


dist, parent = dijkstra()
order = []
now = E
while now:
    order.append(now)
    now = parent[now]

print(dist)
print(len(order))
print(*order[::-1])
