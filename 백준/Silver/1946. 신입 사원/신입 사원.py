from sys import stdin
from heapq import heappop, heappush

input = stdin.readline
T = int(input())


def solve():
    nums = []
    answer = 1

    for n in range(int(input())):
        heappush(nums, tuple(map(int, input().split())))
    
    min_right_score = heappop(nums)[1]

    while nums:
        new_right_score = heappop(nums)[1]
        if new_right_score < min_right_score:
            answer += 1
            min_right_score = new_right_score
    print(answer)




for _ in range(T):
    solve()
