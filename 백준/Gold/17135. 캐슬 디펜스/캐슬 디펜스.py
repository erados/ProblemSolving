from sys import stdin
from itertools import combinations
from collections import deque

input = stdin.readline

N, M, D = map(int, input().split())

graph = []
moves = [
    (0, -1),
    (1, 0),
    (0, 1),
]


def shoot(archer, line):
    q = deque([(line, archer, 0)])
    visited = [False] * (M * N)

    while q:
        y, x, d = q.popleft()

        if y > line and graph[y][x]:
            dead_monster.add((y, x))
            break
        for dy, dx in moves:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M and d < D and not visited[ny * M + nx]:
                visited[ny * M + nx] = True
                q.append((ny, nx, d + 1))


for n in range(N):
    graph.append(list(map(int, input().split())))
graph = graph[::-1]

max_point = 0
for comb in combinations(range(M), 3):
    dead_monster = set()
    for line in range(-1, N):
        for archer in comb:
            shoot(archer, line)

        for y, x in dead_monster:
            graph[y][x] = 0

    for y, x in dead_monster:
        graph[y][x] = 1
    if len(dead_monster) > max_point:
        max_point = len(dead_monster)

print(max_point)
