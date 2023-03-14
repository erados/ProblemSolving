from sys import stdin

input = stdin.readline

N, M, K = map(int, input().split())
moves = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0),
]
graph = [[0] * M for _ in range(N)]
traps = []


def dfs(y, x):
    q = [(y, x)]
    count = 0
    while q:
        y, x = q.pop()
        count += 1
        for dy, dx in moves:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx]:
                q.append((ny, nx))
                graph[ny][nx] = 0

    return count


for k in range(K):
    y, x = map(int, input().split())
    graph[y - 1][x - 1] = 1
    traps.append((y - 1, x - 1))

answer = 0
while traps:
    y, x = traps.pop()
    if graph[y][x]:
        graph[y][x] = 0
        temp = dfs(y, x)
        if answer < temp:
            answer = temp
print(answer)
