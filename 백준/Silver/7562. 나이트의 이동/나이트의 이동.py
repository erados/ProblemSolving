from sys import stdin
from collections import deque

input = stdin.readline

moves = [
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
]


def solve():
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    q = deque([(sx, sy)])

    while q:
        sx, sy = q.popleft()
        if sy == ey and sx == ex:
            return visited[ey][ex]

        for dx, dy in moves:
            nx, ny = sx + dx, sy + dy

            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = visited[sy][sx] + 1
                q.append((nx, ny))
    return -1


T = int(input())

for t in range(T):
    print(solve())
