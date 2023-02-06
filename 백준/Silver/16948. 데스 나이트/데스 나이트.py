from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

moves = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, 0), (2, 0)]
q = deque([(r1, c1, 0)])
visited = [[False] * N for _ in range(N)]

while q:
    y, x, time = q.popleft()

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if (ny, nx) == (r2, c2):
                print(time + 1)
                exit()

            if not visited[ny][nx]:
                q.append((ny, nx, time + 1))
                visited[ny][nx] = True

print(-1)
