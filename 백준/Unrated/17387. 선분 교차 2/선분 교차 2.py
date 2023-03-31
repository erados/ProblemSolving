from sys import stdin

input = stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


def cross_prod(x1, y1, x2, y2, ox, oy):
    return (x1 - ox) * (y2 - oy) - (x2 - ox) * (y1 - oy)


a = cross_prod(x2, y2, x3, y3, x1, y1)
b = cross_prod(x2, y2, x4, y4, x1, y1)

c = cross_prod(x4, y4, x1, y1, x3, y3)
d = cross_prod(x4, y4, x2, y2, x3, y3)

ab = a * b
cd = c * d

if 0 < ab or 0 < cd:
    print(0)
elif ab == 0 and cd == 0:
    x = sorted([x1, x2, x3, x4])
    y = sorted([y1, y2, y3, y4])

    if (
        (sorted([x1, x2]) == x[:2] or sorted([x1, x2]) == x[2:])
        and (sorted([y1, y2]) == y[:2] or sorted([y1, y2]) == y[2:])
        and (x[1] != x[2] or y[1] != y[2])
    ):
        print(0)
    else:
        print(1)
else:
    print(1)
