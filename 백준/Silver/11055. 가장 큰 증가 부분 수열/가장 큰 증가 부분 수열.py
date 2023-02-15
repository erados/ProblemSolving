from sys import stdin

input = stdin.readline

N = int(input())

nums = list(map(int, input().split()))

dp = nums.copy()

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            if dp[i] < nums[i] + dp[j]:
                dp[i] = nums[i] + dp[j]

print(max(dp))
