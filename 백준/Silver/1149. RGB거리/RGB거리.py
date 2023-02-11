from sys import stdin

input = stdin.readline

N = int(input())

costs = []


def _min(a, b):
    return b if b < a else a


for n in range(N):
    costs.append(list(map(int, input().split())))

dp = costs[-1]
for i in range(N - 2, -1, -1):
    temp_dp = [
        costs[i][0] + _min(dp[1], dp[2]),
        costs[i][1] + _min(dp[0], dp[2]),
        costs[i][2] + _min(dp[0], dp[1]),
    ]
    dp = temp_dp
print(min(dp))
