from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

A = set(input().split())
B = set(input().split()).union(A)

print(2 * len(B) - N - M)
