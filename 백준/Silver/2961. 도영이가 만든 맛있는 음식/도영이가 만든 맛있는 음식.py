from sys import stdin

input = stdin.readline

N = int(input())

ingredients = []

for _ in range(N):
    ingredients.append(tuple(map(int, input().split())))
ans = 10**9


def solve(index, s, b):
    global ans
    for idx, (sourness, bitterness) in enumerate(ingredients[index:]):
        sour = sourness * s
        bitter = bitterness + b
        ans = min(abs(sour - bitter), ans)
        if ans == 0:
            return
        solve(index + idx + 1, sour, bitter)
        sour = s
        bitter = b
    return


solve(0, 1, 0)
print(ans)
