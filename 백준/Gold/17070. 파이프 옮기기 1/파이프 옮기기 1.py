from sys import stdin
from pprint import pprint

input = stdin.readline

N = int(input())

# 0 : nothing, 1 : 벽, 2 : 가로, 3 : 대각선, 4 : 세로
graph = [[[0] * 5 for c in range(N)] for r in range(N)]

for r in range(N):
    row = input().split()
    for c in range(N):
        if row[c] == "1":
            graph[r][c][1] = 1

graph[0][1][2] = 1


def solve():
    for y in range(0, N):
        for x in range(2, N):
            if not graph[y][x][1]:
                if y > 0:
                    if not graph[y - 1][x][1] and not graph[y][x - 1][1]:
                        graph[y][x][3] = sum(graph[y - 1][x - 1][2:])
                    graph[y][x][4] = sum(graph[y - 1][x][3:])
                graph[y][x][2] = sum(graph[y][x - 1][2:4])

    print(sum(graph[y][x][2:]))


solve()
