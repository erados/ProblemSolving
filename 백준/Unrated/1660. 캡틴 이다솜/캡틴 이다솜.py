from sys import maxsize

N = int(input())

dp = [0] + [maxsize] * N
balls = [1, 4]
for i in range(1, N + 1):
    j = 1
    if i == balls[-1]:
        k = len(balls) + 1
        balls.append(int(k * (k + 1) * (k + 2) / 6))
    for ball in balls[:-1]:
        temp = dp[i - ball] + 1
        if temp < dp[i]:
            dp[i] = temp
print(dp[-1])
