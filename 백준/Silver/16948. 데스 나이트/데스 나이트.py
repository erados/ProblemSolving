from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

moves = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, 0), (2, 0)]
q = deque([(r1, c1)])
visited = [[0] * N for _ in range(N)]

while q:
    y, x = q.popleft()

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if ny == r2 and nx == c2:
                print(visited[y][x] + 1)
                exit()

            if not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

print(-1)
