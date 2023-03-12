from sys import stdin, maxsize

input = stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left_idx = 0
right_idx = 0
_sum = 0
answer = maxsize

while right_idx <= N:
    if _sum < S:
        if right_idx == N:
            break
        _sum += nums[right_idx]
        right_idx += 1
    elif S <= _sum:
        new_answer = right_idx - left_idx
        if new_answer < answer:
            answer = new_answer
        _sum -= nums[left_idx]
        left_idx += 1

print(0 if answer == maxsize else answer)
