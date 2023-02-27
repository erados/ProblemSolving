from sys import stdin
from math import ceil

input = stdin.readline


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


X, Y = map(int, input().split())
if Y < X:
    X, Y = Y, X

C = gcd(Y, X)
y = Y // C
x = X // C

print((x + y - 1) * C)
