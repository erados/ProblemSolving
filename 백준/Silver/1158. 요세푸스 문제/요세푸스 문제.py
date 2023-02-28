from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
answer = []

nums = list(range(1, N + 1))
idx = 0
while nums:
    idx += K - 1
    idx %= len(nums)
    answer.append(nums.pop(idx))

print("<" + ", ".join(map(str, answer)) + ">")
