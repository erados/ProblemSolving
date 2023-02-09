from sys import stdin

input = stdin.readline

N, K = map(int, input().split())

stack = []
count = 0
for index, n in enumerate(input()[:-1]):
    while stack and stack[-1] < n and count < K:
        stack.pop()
        count += 1
    stack.append(n)


print("".join(stack)[: N - K])
