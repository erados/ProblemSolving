from sys import stdin

input = stdin.readline

N = int(input())
moves = [
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
]
chess = []
possible_positions = [[] for _ in range(2)]

for n in range(N):
    chess.append([0 if c == "1" else 1 for c in input().split()])
    for x in range(N):
        if chess[n][x] == 0:
            possible_positions[(n + x) % 2].append((n, x))


def change_chess(y, x, value):
    chess[y][x] += value
    for dy, dx in moves:
        nx, ny = x + dx, y + dy
        while 0 <= ny < N and 0 <= nx < N:
            chess[ny][nx] += value
            nx, ny = nx + dx, ny + dy


answer = [0, 0]
count = [0, 0]
# i 번째 possible_position 에 말을 두는 경우
def solve(i, black):
    if answer[black] < count[black]:
        answer[black] = count[black]
    if i == len(possible_positions[black]):
        return
    y, x = possible_positions[black][i]
    if chess[y][x] == 0:
        change_chess(y, x, 1)
        count[black] += 1
        solve(i + 1, black)
        count[black] -= 1
        change_chess(y, x, -1)
    solve(i + 1, black)


solve(0, 0)
solve(0, 1)
print(sum(answer))
