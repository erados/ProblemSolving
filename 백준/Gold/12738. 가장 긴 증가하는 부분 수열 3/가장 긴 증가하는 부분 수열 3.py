from sys import stdin
from bisect import bisect_left

input = stdin.readline

N = int(input())
nums = list(map(int, input().split()))
stack = [nums[0]]

for num in nums[1:]:
    if stack[-1] < num:
        stack.append(num)
    else:
        stack[bisect_left(stack, num)] = num
print(len(stack))
