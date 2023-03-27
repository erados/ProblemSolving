from sys import stdin

input = stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))

answer = (nums[0], nums[1], nums[N - 1])
last_sum = nums[0] + nums[1] + nums[N - 1]
for idx in range(N - 2):
    left = idx + 1
    right = N - 1
    _sum = nums[idx] + nums[left] + nums[right]

    if abs(_sum) < abs(last_sum):
        answer = (nums[idx], nums[left], nums[right])
        last_sum = _sum

    while left < right - 1:
        if _sum < 0:
            _sum -= nums[left]
            left += 1
            _sum += nums[left]
        else:
            _sum -= nums[right]
            right -= 1
            _sum += nums[right]

        if abs(_sum) < abs(last_sum):
            answer = (nums[idx], nums[left], nums[right])
            last_sum = _sum
print(*answer)
