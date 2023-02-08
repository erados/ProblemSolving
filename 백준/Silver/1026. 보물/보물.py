input()
sum = 0

for a, b in zip(
    sorted(list(map(int, input().split()))),
    sorted(list(map(int, input().split())), reverse=True),
):
    sum += a * b

print(sum)
