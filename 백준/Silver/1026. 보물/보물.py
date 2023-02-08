from sys import stdin

input = stdin.readline
input()

print(
    sum(
        [
            t[0] * t[1]
            for t in zip(
                sorted(list(map(int, input().split()))),
                sorted(list(map(int, input().split())), reverse=True),
            )
        ]
    )
)
