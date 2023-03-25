from sys import stdin
from heapq import heappop, heappush

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    # 남은 부모 노드의 수, 다음 노드의 인덱스
    graph = [[0, []] for _ in range(N + 1)]
    graph[0][0] -= 1

    for m in range(M):
        a, b = map(int, input().split())
        graph[b][0] += 1
        graph[a][1].append(b)

    heap = []
    for idx in range(1, N + 1):
        p, _ = graph[idx]
        if p == 0:
            heappush(heap, idx)

    answer = []
    for _ in range(N):
        idx = heappop(heap)
        answer.append(idx)
        for next_idx in graph[idx][1]:
            graph[next_idx][0] -= 1
            if graph[next_idx][0] == 0:
                heappush(heap, next_idx)
    print(*answer)


solve()
