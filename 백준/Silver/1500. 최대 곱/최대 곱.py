from sys import stdin
from math import pow

input = stdin.readline

N, S = map(int, input().split())

divisor, remainder = divmod(N, S)

print(int(pow(divisor, S - remainder) * pow(divisor + 1, remainder)))
