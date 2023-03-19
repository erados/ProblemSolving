N = int(input())

dp = [[[0] * 10 for _ in range(2**10)] for __ in range(2)]

for i in range(1, 10):
    dp[0][1 << i][i] = 1

for iter in range(1, N):
    for bitmask in range(2**10):
        for last_num in range(10):
            last = dp[(iter - 1) & 1][bitmask][last_num] % 10**9

            if 0 < last_num:
                dp[iter & 1][bitmask | (1 << (last_num - 1))][last_num - 1] += last
            if last_num < 9:
                dp[iter & 1][bitmask | (1 << (last_num + 1))][last_num + 1] += last

            dp[(iter - 1) & 1][bitmask][last_num] = 0

print(sum(dp[(N - 1) & 1][2**10 - 1]) % 10**9)
