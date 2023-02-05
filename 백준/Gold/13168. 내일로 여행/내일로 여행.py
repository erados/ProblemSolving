from sys import stdin, maxsize

input = stdin.readline
free = [
    "ITX-Saemaeul",
    "ITX-Cheongchun",
    "Mugunghwa",
]
half = [
    "S-Train",
    "V-Train",
]

N, R = map(int, input().split())

cities = {k: v for v, k in enumerate(set(input().split()))}
N = len(cities)

M = int(input())
traval_order = input().split()

K = int(input())
costs = [[maxsize] * N for _ in range(N)]
costs_r = [[maxsize] * N for _ in range(N)]
for _ in range(K):
    type, start, end, cost = input().split()
    cost = int(cost)
    start = cities[start]
    end = cities[end]
    new_cost = cost
    if type in free:
        new_cost = 0
    elif type in half:
        new_cost = cost / 2

    costs[start][end] = min(cost, costs[start][end])
    costs[end][start] = costs[start][end]
    costs_r[start][end] = min(new_cost, costs_r[start][end])
    costs_r[end][start] = costs_r[start][end]


for _c in [costs, costs_r]:
    for city_k in range(N):
        for city_i in range(N):
            for city_j in range(N):
                if _c[city_i][city_j] > _c[city_i][city_k] + _c[city_k][city_j]:
                    _c[city_i][city_j] = _c[city_i][city_k] + _c[city_k][city_j]

result = [0, R]
for idx in range(2):
    _c = [costs, costs_r][idx]
    for index, city in enumerate(traval_order):
        if index < len(traval_order) - 1:
            result[idx] += _c[cities[city]][cities[traval_order[index + 1]]]

print("Yes" if result[1] < result[0] else "No")
