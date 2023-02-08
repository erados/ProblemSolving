from sys import stdin

input = stdin.readline


def solve():
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    count = 0
    for n in range(N):
        cx, cy, r = map(int, input().split())
        count += is_inside(x1, y1, cx, cy, r) ^ is_inside(x2, y2, cx, cy, r)
    print(count)


def is_inside(x, y, cx, cy, r):
    return (x - cx) * (x - cx) + (y - cy) * (y - cy) < r * r


T = int(input())

for t in range(T):
    solve()
