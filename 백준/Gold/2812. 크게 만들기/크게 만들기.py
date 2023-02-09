from sys import stdin

input = stdin.readline

N, K = map(int, input().split())


def solve():
    stack = []
    count = 0
    for n in input().rstrip():
        while stack and stack[-1] < n and count < K:
            stack.pop()
            count += 1
        stack.append(n)

    print("".join(stack)[: N - K])


solve()
