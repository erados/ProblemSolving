from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

N = int(input())

pillar = []
for n in range(N):
    x, y = map(int, input().split())
    heappush(pillar, (-y,x))

main = heappop(pillar)

size = main[0]
left = main[1]
right = main[1]

while pillar:
    y, x = heappop(pillar)
    if left < x < right:
        continue
    if x < left:
        size += (left-x) * y
        left = x
    else:
        size += (x - right) * y
        right = x

print(-size)