from sys import stdin
from itertools import combinations
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
graph = []
moves = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

pos_empty = []
pos_twos = []
for n in range(N):
    row = [*map(int, input().split())]
    for m in range(M):
        if row[m] == 0:
            pos_empty.append((n, m))
        elif row[m] == 2:
            pos_twos.append((n, m))

    graph.append(row)


def bfs():
    q = deque(pos_twos)
    visited = [False] * (M * N)
    cnt = 0
    while q:
        y, x = q.popleft()
        for dy, dx in moves:
            ny = y + dy
            nx = x + dx

            if (
                0 <= ny < N
                and 0 <= nx < M
                and graph[ny][nx] == 0
                and not visited[nx + ny * M]
            ):
                visited[nx + ny * M] = True  # set 과 dict 과 list 성능차이 ?
                cnt += 1
                if cnt > min_cnt_twos:
                    return 100

                q.append((ny, nx))
    return cnt


min_cnt_twos = 100
for comb in combinations(pos_empty, 3):
    for y, x in comb:
        graph[y][x] = 1

    temp = bfs()
    if min_cnt_twos > temp:
        min_cnt_twos = temp

    for y, x in comb:
        graph[y][x] = 0

print(len(pos_empty) - 3 - min_cnt_twos)
