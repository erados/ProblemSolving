from sys import stdin

input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))

answer_1 = 1
answer_1_candidate = 1
answer_2 = 1
answer_2_candidate = 1

for idx in range(1, N):
    if nums[idx - 1] <= nums[idx]:
        answer_1_candidate += 1
    else:
        if answer_1 < answer_1_candidate:
            answer_1 = answer_1_candidate
        answer_1_candidate = 1

for idx in range(1, N):
    if nums[idx] <= nums[idx - 1]:
        answer_2_candidate += 1
    else:
        if answer_2 < answer_2_candidate:
            answer_2 = answer_2_candidate
        answer_2_candidate = 1


print(max(answer_1, answer_1_candidate, answer_2, answer_2_candidate))
