A, B = map(int, input().split())
N = int(input())

ans = abs(A - B)
for _ in range(N):
    ans = min(abs(B - int(input())) + 1, ans)
print(ans)
