from sys import stdin

input = stdin.readline

N = int(input())

arr = sorted(list(map(int, input().split())))

left = 0
right = N - 1

_sum = arr[left] + arr[right]
answer = _sum
pos = (arr[left], arr[right])
while left < right - 1:
    if _sum < 0:
        _sum -= arr[left]
        left += 1
        _sum += arr[left]
    else:
        _sum -= arr[right]
        right -= 1
        _sum += arr[right]

    if abs(_sum) < abs(answer):
        answer = _sum
        pos = (arr[left], arr[right])

print(*pos)
