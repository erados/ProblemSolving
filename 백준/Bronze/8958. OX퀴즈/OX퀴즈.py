from sys import stdin

input = stdin.readline

T = int(input())


for _ in range(T):
    ans = input().rstrip()

    result = 0
    score = 1
    for c in ans:
        if c == "O":
            result += score
            score += 1
        else:
            score = 1
    print(result)
