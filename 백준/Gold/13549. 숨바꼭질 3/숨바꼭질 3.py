import sys
from collections import deque

input = sys.stdin.readline

# S, E = map(int, input().split())
def solve(S, E):

    b_S, b_E = bin(S)[2:], bin(E)[2:]

    if S >= E:
        return S - E

    print(b_S, b_E)

    return min(
        abs(int(b_E[: len(b_S)], 2) - int(b_S, 2)), (int(b_E[: len(b_S)] + "0", 2) - S)
    ) + b_E[len(b_S) :].count("1")


def solve2(S, E):
    q = deque([(0, S)])
    visited = [False] * 200001
    visited[S] = True

    while q:
        time, now = q.popleft()
        if now == E:
            return time
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


S, E = map(int, input().split())
print(solve2(S, E))
