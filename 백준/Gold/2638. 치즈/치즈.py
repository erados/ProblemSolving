from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

moves = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

graph = []

for n in range(N):
    graph.append([*map(lambda x: 4 if x == "1" else 0, input().split())])


def dfs():
    q = [(0, 0)]
    visited = [[False] * M for n in range(N)]
    visited[0][0] = True

    while q:
        y, x = q.pop()

        for dy, dx in moves:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0:
                    if not visited[ny][nx]:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                else:
                    graph[ny][nx] -= 1

    for n in range(N):
        graph[n] = [*map(lambda x: 0 if x <= 2 else 4, graph[n])]

    for row in visited:
        if sum(row) != M:
            return True
    return False


time = 0
while dfs():
    time += 1

print(time)
