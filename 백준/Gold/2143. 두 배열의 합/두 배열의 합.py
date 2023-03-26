from sys import stdin
from collections import defaultdict

input = stdin.readline

T = int(input())

sum_dict1 = defaultdict(int)

N = int(input())
arr1 = list(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split()))


for left in range(N):
    _sum = 0
    for right in range(left, N):
        _sum += arr1[right]
        sum_dict1[_sum] += 1

answer = 0
for left in range(M):
    _sum = 0
    for right in range(left, M):
        _sum += arr2[right]
        answer += sum_dict1[T - _sum]
print(answer)
