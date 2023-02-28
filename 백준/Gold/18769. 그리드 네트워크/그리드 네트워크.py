from sys import stdin
from heapq import heappop, heappush

input = stdin.readline
T = int(input())


def solve():
    R, C = map(int, input().split())
    cost_row = []
    cost_col = []

    visited = [[False] * C for _ in range(R)]
    candidate_edges = []

    for r in range(R):
        cost_row.append(list(map(int, input().split())))
    for c in range(R - 1):
        cost_col.append(list(map(int, input().split())))

    heappush(candidate_edges, (0, 0, 0))

    total_cost = 0
    count = 0
    while count < R * C:
        cost, y, x = heappop(candidate_edges)
        if not visited[y][x]:
            count += 1
            total_cost += cost
            visited[y][x] = True
            if x < C - 1 and not visited[y][x + 1]:
                heappush(candidate_edges, (cost_row[y][x], y, x + 1))
            if x > 0 and not visited[y][x - 1]:
                heappush(candidate_edges, (cost_row[y][x - 1], y, x - 1))
            if y < R - 1 and not visited[y + 1][x]:
                heappush(candidate_edges, (cost_col[y][x], y + 1, x))
            if y > 0 and not visited[y - 1][x]:
                heappush(candidate_edges, (cost_col[y - 1][x], y - 1, x))

    return total_cost


for _ in range(T):
    print(solve())
