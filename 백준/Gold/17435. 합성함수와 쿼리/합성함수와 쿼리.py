from sys import stdin

input = stdin.readline
ans = []

M = int(input())
dp = [[0, *map(int, input().split())]]


# dp[i][x] 를 반환하는 함수
def get(i, x):
    if len(dp) > i:
        return dp[i][x]

    while i >= len(dp):
        dp.append([dp[-1][x] for x in dp[-1]])

    return dp[i][x]


# f_n(x) 를 반환하는 함수
def solve(n, x):
    i = 0
    ans = x
    while n >= (1 << i):
        if n & (1 << i):
            ans = get(i, ans)
        i += 1
    return ans


Q = int(input())

for q in range(Q):
    n, x = map(int, input().split())
    print(solve(n, x))
