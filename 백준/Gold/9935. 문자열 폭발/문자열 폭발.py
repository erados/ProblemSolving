from sys import stdin

input = stdin.readline

word = input().rstrip()
bomb = [c for c in input().rstrip()]
bomb_last = bomb[-1]
n_len_bomb = -len(bomb)
stack = []

for c in word:
    stack.append(c)
    if c == bomb_last:
        if stack[n_len_bomb:] == bomb:
            del stack[n_len_bomb:]
print("".join(stack) if stack else "FRULA")
