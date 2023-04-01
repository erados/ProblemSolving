from sys import stdin

input = stdin.readline

N = int(input())
paper = [[0] * 100 for _ in range(100)]

for n in range(N):
    x, y = map(int, input().split())
    for ny in range(y, y + 10):
        paper[ny][x : x + 10] = [1] * 10


print(sum(map(sum, paper)))
