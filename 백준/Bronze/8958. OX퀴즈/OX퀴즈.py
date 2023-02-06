import sys

for _ in range(int(sys.stdin.readline())):
    score = 0
    for c in sys.stdin.readline()[:-1].split("X"):
        score += len(c) * (len(c) + 1) // 2

    print(score)
