import sys
from collections import deque

input = sys.stdin.readline


def solve2():
    S, E = map(int, input().split())

    q = deque([(0, S)])
    visited = [False] * 200001
    visited[S] = True

    while q:
        time, now = q.popleft()
        if now == E:
            print(time)
            return
        if now < E:
            if not visited[now * 2]:
                q.appendleft((time, now * 2))
                visited[now * 2] = True
            if not visited[now + 1]:
                q.append((time + 1, now + 1))
                visited[now + 1] = True
        if now > 0 and not visited[now - 1]:
            q.append((time + 1, now - 1))
            visited[now - 1] = True


solve2()
