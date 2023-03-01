import sys

input = sys.stdin.readline
last_city = None
INF = 10**5
N = int(input())
M = int(input())

graph = [[INF] * N for _ in range(N)]

for i in range(N):
    graph[i] = list(map(lambda x: int(x) if x != "0" else INF, input().split()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for city in map(int, input().split()):
    if last_city != None and graph[last_city][city - 1] == INF:
        if last_city == city - 1:
            continue
        print("NO")
        exit(0)
    last_city = city - 1

print("YES")
