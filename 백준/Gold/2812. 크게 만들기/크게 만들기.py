from sys import stdin

input = stdin.readline

N, K = map(int, input().split())

stack = []

for index, n in enumerate(input()[:-1]):
    while stack and stack[-1] < n and len(stack) > index - K:
        stack.pop()
    stack.append(n)


print("".join(map(str, stack))[: N - K])
