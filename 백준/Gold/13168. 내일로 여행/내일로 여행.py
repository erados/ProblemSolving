from sys import stdin, maxsize
from pprint import pprint

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
costs = [[5000000] * N for _ in range(N)]
costs_r = [[5000000] * N for _ in range(N)]
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


for city_k in range(N):
    for city_i in range(N):
        for city_j in range(N):
            if costs[city_i][city_j] > costs[city_i][city_k] + costs[city_k][city_j]:
                costs[city_i][city_j] = costs[city_i][city_k] + costs[city_k][city_j]

for city_k in range(N):
    for city_i in range(N):
        for city_j in range(N):
            if (
                costs_r[city_i][city_j]
                > costs_r[city_i][city_k] + costs_r[city_k][city_j]
            ):
                costs_r[city_i][city_j] = (
                    costs_r[city_i][city_k] + costs_r[city_k][city_j]
                )

cost1 = 0
for index, city in enumerate(traval_order):
    if index < len(traval_order) - 1:
        cost1 += costs[cities[city]][cities[traval_order[index + 1]]]

cost2 = R
for index, city in enumerate(traval_order):
    if index < len(traval_order) - 1:
        cost2 += costs_r[cities[city]][cities[traval_order[index + 1]]]

print("Yes" if cost2 < cost1 else "No")
