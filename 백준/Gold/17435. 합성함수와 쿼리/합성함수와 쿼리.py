from sys import stdin

input = stdin.readline
ans = []

M = int(input())
dp = [[0] * (M + 1) for _ in range(19)]
dp[0] = [0] + list(map(int, input().split()))


# dp[i][x] 를 반환하는 함수
def get(i, x):
    if dp[i][x]:
        return dp[i][x]

    index = 0
    while i > index:
        if not dp[index + 1][x]:
            dp[index + 1][x] = get(index, get(index, x))
        index += 1

    return dp[index][x]


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
