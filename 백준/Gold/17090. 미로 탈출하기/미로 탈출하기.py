from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

N, M = map(int, input().split())

graph = []
move = {
    'U' : (-1,0),
    'D' : (1,0),
    'L' : (0,-1),
    'R' : (0,1),
}

for n in range(N):
    graph.append(input().rstrip())

dp = [[-1] * M for _ in range(N)]

def check(y, x):
    if not (0<=y<N and 0<=x<M):
        return 1
    elif dp[y][x] != -1:
        return dp[y][x]
    dy, dx = move[graph[y][x]]
    dp[y][x] = 0
    dp[y][x] = check(y+dy,x+dx)

    return dp[y][x]
answer = 0
for n in range(N):
    for m in range(M):
        if dp[n][m] == -1:
            check(n,m)
        answer += dp[n][m]

print(answer)