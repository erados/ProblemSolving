from sys import stdin
from collections import deque

input = stdin.readline

M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]
moves = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]

tomatos = []
last_tomatos = 0
for h in range(H):
    for n in range(N):
        row = list(map(int, input().split()))
        for cell_idx in range(M):
            if row[cell_idx] == 1:
                tomatos.append((h, n, cell_idx, 0))
            elif row[cell_idx] == 0:
                last_tomatos += 1
        graph[h].append(row)


def bfs():
    global last_tomatos
    q = deque(tomatos)
    time = 0
    if last_tomatos:
        while q:
            z, y, x, time = q.popleft()

            for dz, dy, dx in moves:
                nz = z + dz
                ny = y + dy
                nx = x + dx

                if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                    if graph[nz][ny][nx] == 0:
                        graph[nz][ny][nx] = 1
                        last_tomatos -= 1
                        q.append((nz, ny, nx, time + 1))

    if last_tomatos:
        return -1

    return time


print(bfs())
