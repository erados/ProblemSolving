from sys import stdin

input = stdin.readline

N = int(input())

#  0 : 벽, 1 : 가로, 2 : 대각선, 3 : 세로
graph = [[[0] * 4 for c in range(N)] for r in range(N)]

for r in range(N):
    row = input().split()
    for c in range(N):
        if row[c] == "1":
            graph[r][c][0] = 1

graph[0][1][1] = 1


def solve():
    for y in range(0, N):
        for x in range(2, N):
            if not graph[y][x][0]:
                if y > 0:
                    if not graph[y - 1][x][0] and not graph[y][x - 1][0]:
                        graph[y][x][2] = sum(graph[y - 1][x - 1][1:])
                    graph[y][x][3] = sum(graph[y - 1][x][2:])
                graph[y][x][1] = sum(graph[y][x - 1][1:3])

    print(sum(graph[y][x][1:]))


solve()
