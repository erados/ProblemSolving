from sys import stdin

input = stdin.readline
prime = 1_000_000_007


def get_inverse(num):
    bin_goal = bin(prime - 2)[2:]

    inverse = 1
    for i in bin_goal:
        inverse *= inverse
        if i == "1":
            inverse *= num
        inverse %= prime

    return inverse


ans = 0
for _ in range(int(input())):
    N, S = map(int, input().split())
    ans += S * get_inverse(N)
    ans %= prime

print(ans)
