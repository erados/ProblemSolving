from sys import stdin, maxsize

input = stdin.readline
T = int(input())


def solve():
    nums = []
    answer = 0
    N = int(input())
    for n in range(N):
        nums.append(tuple(map(int, input().split())))
    nums.sort()
    
    min_right_score = maxsize

    for n in range(N):
        new_right_score = nums[n][1]
        if new_right_score < min_right_score:
            answer += 1
            min_right_score = new_right_score
    print(answer)




for _ in range(T):
    solve()
