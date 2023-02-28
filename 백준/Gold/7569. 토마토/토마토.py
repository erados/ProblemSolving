from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

tomatos = [[list(map(int, input().split())) for n in range(N)] for h in range(H)]

moves = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

to_visit = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatos[h][n][m] == 1:
                to_visit.append((m, n, h, 0))

while to_visit:
    target = to_visit.popleft()
    m, n, h, time = target
    for move in moves:
        nm = m + move[0]
        nn = n + move[1]
        nh = h + move[2]
        ntime = time + 1
        if 0 <= nm < M and 0 <= nn < N and 0 <= nh < H:
            if tomatos[nh][nn][nm] == 0:
                tomatos[nh][nn][nm] = 1
                to_visit.append((nm, nn, nh, ntime))

num_of_zero = sum(sum(tomatos, []), []).count(0)
if num_of_zero > 0:
    print(-1)
else:
    print(time)
