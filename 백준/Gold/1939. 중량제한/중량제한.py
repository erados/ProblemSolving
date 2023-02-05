from sys import stdin
from collections import defaultdict

input = stdin.readline

N, M = map(int, input().split())
graph = defaultdict(dict)
ans = 0

for _ in range(M):
    A, B, C = map(int, input().split())

    if B in graph[A]:
        C = max(C, graph[A][B])

    graph[A][B] = C
    graph[B][A] = C

S, E = map(int, input().split())


def dfs(start, weight):
    visited = [False] * (N + 1)
    visited[start] = True
    q = [start]

    while q:
        curr = q.pop()

        for next in graph[curr]:
            if not visited[next]:
                if weight <= graph[curr][next]:
                    if next == E:
                        return True
                    q.append(next)
                    visited[next] = True


    return False

left = 1
right = 10**9
ans = 0
while left <= right:
    mid = (left + right) // 2
    if dfs(S, mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)
