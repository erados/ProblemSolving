from sys import stdin

input = stdin.readline

N = int(input())
answer = {
    1: 0,
    0: 0,
    -1: 0,
}
board = []
for n in range(N):
    board.append(list(map(int, input().split())))


def solve(sy, sx, size):
    if size == 1:
        answer[board[sy][sx]] += 1
        return board[sy][sx]

    nsize = size // 3
    temp = {
        solve(ny, nx, nsize)
        for nx in range(sx, sx + size, nsize)
        for ny in range(sy, sy + size, nsize)
    }

    if len(temp) == 1 and list(temp)[0] in [-1, 0, 1]:
        answer[board[sy][sx]] -= 8
        return board[sy][sx]

    return 2


solve(0, 0, len(board[-1]))

print(answer[-1])
print(answer[0])
print(answer[1])
