from sys import stdin, maxsize

input = stdin.readline

N = int(input())
costs = []
dp = [{} for _ in range(N)]
INF = maxsize

for _ in range(N):
    costs.append(list(map(int, input().split())))


def solve(now, index):
    if index == (1 << N) - 1:
        return costs[now][0] if costs[now][0] else INF

    if index in dp[now]:
        return dp[now][index]

    dp[now][index] = INF

    for i, value in enumerate(costs[now]):
        if index & (1 << i):
            continue

        if value == 0:
            continue

        temp = solve(i, index | (1 << i))
        dp[now][index] = min(dp[now][index], temp + value)

    return dp[now][index]


print(solve(0, 1))
