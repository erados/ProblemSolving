from sys import stdin
from collections import defaultdict, deque

input = stdin.readline
_MAX = 2500

ipt = input().rstrip()
# start : [end_1, ...]
palindrome = defaultdict(list)

left_idx_queue = deque([])
dp = [_MAX] * len(ipt) + [0]

for idx, curr in enumerate(ipt):
    if 0 < idx:
        left_idx_queue.append(idx)
    if 1 < idx:
        left_idx_queue.append(idx - 1)

    for _ in range(len(left_idx_queue)):
        left_idx = left_idx_queue.popleft()
        if left_idx and ipt[left_idx - 1] == curr:
            palindrome[left_idx - 1].append(idx)
            left_idx_queue.append(left_idx - 1)

for i in range(len(ipt) - 1, -1, -1):
    dp[i] = dp[i + 1] + 1

    for end in palindrome[i]:
        if dp[end + 1] + 1 < dp[i]:
            dp[i] = dp[end + 1] + 1
print(dp[0])
