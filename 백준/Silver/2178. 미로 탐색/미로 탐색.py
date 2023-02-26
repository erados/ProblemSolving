from sys import stdin
from collections import deque

input = stdin.readline

graph = []
moves = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]
N, M = map(int, input().split())

for n in range(N):
    graph.append(input().rstrip())


def bfs():
    q = deque([(0, 0)])
    visited = [0] * (N * M)
    while q:
        y, x = q.popleft()

        if y == N - 1 and x == M - 1:
            print(visited[y * M + x] + 1)
            return

        for dy, dx in moves:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == "1":
                if visited[ny * M + nx]:
                    continue
                q.append((ny, nx))
                visited[ny * M + nx] = visited[y * M + x] + 1


bfs()
