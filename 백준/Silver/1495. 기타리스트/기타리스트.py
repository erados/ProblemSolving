from heapq import heappop, heappush

N, S, M = map(int, input().split())
delta_volumes = list(map(int, input().split()))
candidates = [S]


def solve(delta_volume):
    temp = set()
    while candidates:
        now_volume = candidates.pop()

        if now_volume + delta_volume <= M:
            temp.add(now_volume + delta_volume)

        if -1 < now_volume - delta_volume:
            temp.add(now_volume - delta_volume)
    if temp:
        return list(temp)
    else:
        print(-1)
        exit()


for delta_volume in delta_volumes:
    candidates = solve(delta_volume)

print(max(candidates))
