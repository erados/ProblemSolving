from sys import stdin

input = stdin.readline

N = int(input())
K = int(input())


def count_num_less_or_equal(n):
    answer = 0
    for i in range(1, N + 1):
        temp = n // i
        if temp > N:
            answer += N
        else:
            answer += temp
        if answer > K:
            return K + 1
    return answer


def solve():
    start = 1
    end = N**2

    while start + 1 < end:
        mid = (start + end) // 2
        if count_num_less_or_equal(mid) < K:
            start = mid
        else:
            end = mid
    return end


if K == 1:
    print(1)
else:
    print(solve())
