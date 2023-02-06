from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    ans = input().rstrip().split("X")
    score = 0
    for c in ans:
        score += len(c) * (len(c) + 1) // 2

    print(score)
