from sys import stdin

input = stdin.readline

N = int(input())
total_money = [0] * (N + 1)
for n in range(1, N + 1):
    days, money = map(int, input().split())
    if n + days <= N + 1:
        temp = max(total_money[:n]) + money
        if total_money[n + days - 1] < temp:
            total_money[n + days - 1] = temp
print(max(total_money))
