from sys import stdin

input = stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    nums = [1, 1, 1, 2, 2]

    for i in range(5, N):
        nums[i % 5] = nums[(i + 4) % 5] + nums[i % 5]

    print(nums[(N - 1) % 5])
