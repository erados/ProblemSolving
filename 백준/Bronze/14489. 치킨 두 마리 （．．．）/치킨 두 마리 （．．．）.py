A, B = map(int, input().split())
C = int(input())
_sum = A + B
print(_sum if _sum < 2 * C else _sum - 2 * C)
