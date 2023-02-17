from sys import stdin

input = stdin.readline

word = input().rstrip()
bomb = [c for c in input().rstrip()]

stack = []

for c in word:
    stack.append(c)
    if c == bomb[-1]:
        if len(stack) >= len(bomb):
            if stack[len(stack) - len(bomb) :] == bomb:
                for i in range(len(bomb)):
                    stack.pop()
print("".join(stack) if stack else "FRULA")
