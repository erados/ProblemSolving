from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
ans = 0

for _ in range(M):
    A, B, C = map(int, input().split())

    graph[A].append((B, C))
    graph[B].append((A, C))

S, E = map(int, input().split())


def dfs(start, weight):
    visited = [False] * (N + 1)
    visited[start] = True
    q = [start]

    while q:
        curr = q.pop()

        for next, weight_limit in graph[curr]:
            if not visited[next] and weight <= weight_limit:
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
