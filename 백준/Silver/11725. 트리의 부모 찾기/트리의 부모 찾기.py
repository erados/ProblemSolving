from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**6)
input = stdin.readline


N = int(input())
parent = [0] * (N + 1)
parent[1] = 1

graph = defaultdict(list)

for _ in range(N - 1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

count = 0


def solve(now):
    global count
    if count == N - 1:
        return
    for next in graph[now]:
        if not parent[next]:
            parent[next] = now
            count += 1
            solve(next)


solve(1)

for i in range(2, N + 1):
    print(parent[i])
