from sys import stdin
from collections import defaultdict

input = stdin.readline

N, M = map(int, input().split())

nums = sorted([*map(int, input().split())])
visited = defaultdict(bool)


ans = []
selected = {k: False for k in range(len(nums))}


def permutation(m):

    if m == 0:
        yield tuple(ans)
        return

    for index in range(len(nums)):
        if not selected[index]:
            ans.append(nums[index])
            selected[index] = True
            yield from permutation(m - 1)
            selected[index] = False
            ans.pop()

    return


for comb in permutation(M):
    if not visited[comb]:
        print(*comb)
        visited[comb] = True
