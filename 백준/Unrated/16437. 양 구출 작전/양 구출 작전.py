from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)

input = stdin.readline

N = int(input())

# node = (current_node_idx, wolf(-) or sheep(+))
tree = [[(1, 0)]]

for node_idx in range(2, N + 1):
    t, ap = input().split(maxsplit=1)
    a, p = map(int, ap.split())
    new_node = (node_idx, a if t == "S" else -a)
    for i in range(len(tree), p + 1):
        tree.append([])
    tree[p].append(new_node)

# print(tree)


def solve(idx, value):
    sheep = 0
    if idx < len(tree):
        for new_node_idx, new_node_value in tree[idx]:
            temp = solve(new_node_idx, new_node_value)

            if temp > 0:
                sheep += temp

    return sheep + value


print(solve(1, 0))
