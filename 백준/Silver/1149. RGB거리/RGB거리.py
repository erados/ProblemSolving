from sys import stdin

input = stdin.readline

N = int(input())

dp = []


def _min(a, b):
    return b if b < a else a


dp = list(map(int, input().split()))
for i in range(1, N):
    cost = list(map(int, input().split()))
    dp = [
        cost[0] + _min(dp[1], dp[2]),
        cost[1] + _min(dp[0], dp[2]),
        cost[2] + _min(dp[0], dp[1]),
    ]

print(min(dp))
