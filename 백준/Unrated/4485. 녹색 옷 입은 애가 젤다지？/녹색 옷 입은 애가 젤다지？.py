from sys import stdin, maxsize
from heapq import heappush, heappop

input = stdin.readline
problem_num = 1
moves = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

while True:
    N = int(input())
    if N == 0:
        exit()
    graph = []
    dp = [[maxsize] * N for _ in range(N)]

    for n in range(N):
        graph.append(list(map(int, input().split())))
    dp[0][0] = graph[0][0]
    # y, x
    q = [(graph[0][0], 0, 0)]

    while q:
        current_loopy, y, x = heappop(q)

        for dy, dx in moves:
            ny = y + dy
            nx = x + dx

            if (
                0 <= ny < N
                and 0 <= nx < N
                and current_loopy + graph[ny][nx] < dp[ny][nx]
            ):
                dp[ny][nx] = dp[y][x] + graph[ny][nx]
                heappush(q, (dp[y][x] + graph[ny][nx], ny, nx))
    print(f"Problem {problem_num}: {dp[-1][-1]}")
    problem_num += 1
