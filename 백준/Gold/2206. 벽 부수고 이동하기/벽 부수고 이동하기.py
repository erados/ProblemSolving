from sys import stdin, maxsize
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
graph = []
score_map = [[[maxsize] * M for n in range(N)] for b in range(2)]
score_map[0][0][0] = 1
score_map[1][0][0] = 1
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for n in range(N):
    graph.append(input().rstrip())


def solve():
    # y, x, bomb
    q = deque([(0, 0, 0)])

    while q:
        y, x, bomb = q.popleft()

        if y == N - 1 and x == M - 1:
            return score_map[bomb][y][x]

        for dy, dx in moves:
            ny = y + dy
            nx = x + dx
            n_bomb = bomb
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == "1":
                    if n_bomb:
                        continue
                    else:
                        n_bomb = 1
                if score_map[n_bomb][ny][nx] > score_map[bomb][y][x] + 1:
                    score_map[n_bomb][ny][nx] = score_map[bomb][y][x] + 1
                    q.append((ny, nx, n_bomb))

    return -1


print(solve())
