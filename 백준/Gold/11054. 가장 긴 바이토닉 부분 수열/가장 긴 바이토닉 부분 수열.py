from sys import stdin

input = stdin.readline

N = int(input())
nums = [*map(int, input().split())]
dp_a = [0] * N
dp_d = [0] * N


for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            if dp_a[i] <= dp_a[j]:
                dp_a[i] = dp_a[j] + 1

        if nums[N - 1 - j] < nums[N - 1 - i]:
            if dp_d[N - 1 - i] <= dp_d[N - 1 - j]:
                dp_d[N - 1 - i] = dp_d[N - 1 - j] + 1

print(max([dp_a[i] + dp_d[i] + 1 for i in range(N)]))
