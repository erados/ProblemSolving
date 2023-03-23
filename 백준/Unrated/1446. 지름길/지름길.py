from sys import stdin

input = stdin.readline

# dp[위치] = 걸린 시간
dp = [0]
# 위치 [(e, s, delay), ...]
positions = []

N, D = map(int, input().split())

for _ in range(N):
    s, e, delay = map(int, input().split())
    if D < e:
        continue
    positions.append((e, s, delay))

positions.sort(reverse=True)

for idx in range(1, D + 1):
    dp.append(dp[-1] + 1)
    while positions and positions[-1][0] == idx:
        pos = positions.pop()
        dp[idx] = min(dp[idx], dp[pos[1]] + pos[2])

print(dp[-1])
