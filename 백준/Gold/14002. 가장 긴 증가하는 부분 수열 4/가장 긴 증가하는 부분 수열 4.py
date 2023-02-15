from sys import stdin

input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))
answer = {k: [k] for k in range(N)}
for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            if len(answer[i]) <= len(answer[j]):
                answer[i] = answer[j] + [i]
index = 0
for i in answer:
    l = len(answer[i])
    if len(answer[index]) < l:
        index = i
print(len(answer[index]))
print(*[nums[i] for i in answer[index]])
