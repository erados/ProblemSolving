s, N = input().split()
s = int(s)
N = list(map(int, N))

graph = [
    [[1, 0, 1, 1, 0, 1, 1, 1, 1, 1]],
    [[1, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]],
    [[0, 0, 1, 1, 1, 1, 1, 0, 1, 1]],
    [[1, 0, 1, 0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]],
    [[1, 0, 1, 1, 0, 1, 1, 0, 1, 1]],
]

for y in range(5):
    row = ""
    for n in N:
        if y % 2:
            row += (
                ("|" if graph[y][0][n] else " ")
                + " " * s
                + ("|" if graph[y][1][n] else " ")
                + " "
            )
        else:
            row += " " + ("-" if graph[y][0][n] else " ") * s + "  "
    if y % 2:
        for _ in range(s):
            print(row)
    else:
        print(row)
