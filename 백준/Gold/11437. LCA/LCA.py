from sys import stdin
from collections import deque

input = stdin.readline


def find_co_parent(a, b):
    for i in range(depth[a] - depth[b]):
        a = parent[a]
    for i in range(depth[b] - depth[a]):
        b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [-1] * (N + 1)
depth = [0] * (N + 1)
for n in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([(1, 0)])
while q:
    n, level = q.popleft()
    for child in graph[n]:
        if parent[n] != child:
            parent[child] = n
            depth[child] = level + 1
            q.append((child, level + 1))

M = int(input())

for m in range(M):
    a, b = map(int, input().split())
    print(find_co_parent(a, b))
