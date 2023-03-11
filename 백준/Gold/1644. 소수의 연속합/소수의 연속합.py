from sys import stdin
from math import sqrt

input = stdin.readline

N = int(input())
primes = [2]


def get_prime():
    for num in range(3, 4_000_038):
        sqrt_num = sqrt(num)
        for prime in primes:
            if sqrt_num < prime:
                primes.append(num)
                yield num
                break
            if num % prime == 0:
                break


def solve():
    gp = get_prime()

    left_idx = 0
    _sum = 2
    answer = 0
    while primes[-1] <= N:
        if _sum == N:
            answer += 1
            _sum += next(gp)
        elif _sum < N:
            _sum += next(gp)
        else:
            _sum -= primes[left_idx]
            left_idx += 1

    print(answer)


solve()
