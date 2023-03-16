from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
visited = [False] * (2 * 100000 + 1)

# N, M 에 대해 time 을 반환하는 함수
def solve(N, M):
    q = deque([(N, 0)])
    visited[N] = True
    while q:
        pos, time = q.popleft()
        if pos == M:
            return time
        if pos < M and not visited[pos * 2]:
            visited[pos * 2] = True
            q.append((pos * 2, time + 1))

        if 0 < pos and not visited[pos - 1]:
            visited[pos - 1] = True
            q.append((pos - 1, time + 1))

        if pos < M and not visited[pos + 1]:
            visited[pos + 1] = True
            q.append((pos + 1, time + 1))


print(solve(N, M))
