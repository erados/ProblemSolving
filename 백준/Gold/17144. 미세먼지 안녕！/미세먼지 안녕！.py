from sys import stdin

input = stdin.readline

R, C, T = map(int, input().split())
graph = []
inc_graph = [[0] * C for r in range(R)]
cleaner = []
moves = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

for r in range(R):
    graph.append([*map(int, input().split())])
    if graph[r][0] == -1:
        cleaner.append(r)


def diffusion():
    for y in range(R):
        for x in range(C):
            if graph[y][x] > 4:
                cnt = 0
                diffusion_amount = graph[y][x] // 5
                for dy, dx in moves:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < R and 0 <= nx < C and graph[ny][nx] != -1:
                        cnt += 1
                        inc_graph[ny][nx] += diffusion_amount
                graph[y][x] -= cnt * diffusion_amount

    for y in range(R):
        for x in range(C):
            graph[y][x] += inc_graph[y][x]
            inc_graph[y][x] = 0


def circulate():
    counter_clock_wise_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    clock_wise_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    x, y = 0, cleaner[0]
    i = 0

    while i < 4:
        dy, dx = counter_clock_wise_moves[i]
        ny = y + dy
        nx = x + dx

        if ny == cleaner[0] and nx == 0:
            break

        if 0 <= ny <= cleaner[0] and 0 <= nx < C:
            graph[y][x] = graph[ny][nx]
            y, x = ny, nx
        else:
            i += 1

    x, y = 0, cleaner[1]
    i = 0

    while i < 4:
        dy, dx = clock_wise_moves[i]
        ny = y + dy
        nx = x + dx

        if ny == cleaner[1] and nx == 0:
            break

        if cleaner[1] <= ny < R and 0 <= nx < C:
            graph[y][x] = graph[ny][nx]

            y, x = ny, nx
        else:
            i += 1

    graph[cleaner[0]][0] = -1
    graph[cleaner[0]][1] = 0
    graph[cleaner[1]][0] = -1
    graph[cleaner[1]][1] = 0


for t in range(T):
    diffusion()
    circulate()

print(sum(map(sum, graph)) + 2)
