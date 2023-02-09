from sys import stdin

input = stdin.readline

ans = 0
visited = [False] * 26

R, C = map(int, input().split())

moves = [
    (1, 0),
    (-1, 0),
    (0, -1),
    (0, 1),
]

graph = []

for r in range(R):
    graph.append(input()[:-1])


def solve(x, y, count):
    global ans

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < C and 0 <= ny < R:
            if not visited[ord(graph[ny][nx]) - 65]:
                visited[ord(graph[ny][nx]) - 65] = True
                solve(nx, ny, count + 1)
                visited[ord(graph[ny][nx]) - 65] = False
    if ans < count:
        ans = count


visited[ord(graph[0][0]) - 65] = True
solve(0, 0, 1)
print(ans)
