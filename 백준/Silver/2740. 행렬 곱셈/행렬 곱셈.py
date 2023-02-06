from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
A = []
for n in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for m in range(M):
    B.append(list(map(int, input().split())))

for n in range(N):
    row = []
    for k in range(K):
        row.append(sum([A[n][i] * B[i][k] for i in range(M)]))
    print(*row)
