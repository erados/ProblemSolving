from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dxs = [-1, 1, -1, 1, -2, 2]
dys = [-2, -2, 2, 2, 0, 0]

q = deque([(r1, c1)])
visited = [[0] * N for _ in range(N)]

while q:
    y, x = q.popleft()

    for i in range(6):
        nx = x + dxs[i]
        ny = y + dys[i]

        if 0 <= nx < N and 0 <= ny < N:
            if ny == r2 and nx == c2:
                print(visited[y][x] + 1)
                exit()

            if not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

print(-1)
