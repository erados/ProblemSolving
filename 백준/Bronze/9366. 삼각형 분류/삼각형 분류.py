T = int(input())


for index in range(1, T + 1):
    arr = sorted(list(map(int, input().split())))
    if arr[0] == arr[2]:
        print(f"Case #{index}: equilateral")
    elif arr[0] + arr[1] <= arr[2]:
        print(f"Case #{index}: invalid!")
    elif arr[1] == arr[0] or arr[1] == arr[2]:
        print(f"Case #{index}: isosceles")
    else:
        print(f"Case #{index}: scalene")
