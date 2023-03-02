from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

N = int(input())
nums = []

for num in map(int,input().split()):
    heappush(nums, num)

for n in range(N-1):
    for num in map(int,input().split()):
        if nums[0] < num:
            heappop(nums)
            heappush(nums, num)
print(nums[0])
    
    

