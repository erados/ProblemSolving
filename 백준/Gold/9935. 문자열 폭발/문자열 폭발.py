from sys import stdin

input = stdin.readline

word = input().rstrip()
bomb = [c for c in input().rstrip()]
bomb_last = bomb[-1]
stack = []

for c in word:
    stack.append(c)
    if c == bomb_last and stack[len(stack) - len(bomb) :] == bomb:
        del stack[-len(bomb) :]
print("".join(stack) if stack else "FRULA")
