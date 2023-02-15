from sys import stdin

input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if nums[j] > nums[i]:
            if dp[i] <= dp[j]:
                dp[i] = dp[j] + 1

print(max(dp))
