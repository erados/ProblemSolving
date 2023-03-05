from sys import stdin

input = stdin.readline

N, A, D = map(int, input().split())

answer = 0
next_num = A
for n in map(int, input().split()):
    if next_num == n:
        next_num += D
        answer+=1

print(answer)

