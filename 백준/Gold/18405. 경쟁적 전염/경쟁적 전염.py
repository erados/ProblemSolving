from sys import stdin
from collections import defaultdict, deque

input = stdin.readline
N, K = map(int, input().split())

moves = [
    (1, 0),
    (-1, 0),
    (0, -1),
    (0, 1),
]
q = defaultdict(deque)
graph = []

for r_index in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for c_index, num in enumerate(row):
        if num:
            q[num].append((c_index, r_index))
q = dict(sorted(q.items()))


def solve():
    for s in range(S):
        for num in q:
            for _ in range(len(q[num])):
                x, y = q[num].popleft()
                if y == Y - 1 and x == X - 1:
                    return graph[Y - 1][X - 1]
                for dx, dy in moves:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < N and 0 <= ny < N:
                        if not graph[ny][nx]:
                            graph[ny][nx] = num
                            q[num].append((nx, ny))

    return graph[Y - 1][X - 1]


S, Y, X = map(int, input().split())
print(solve())
