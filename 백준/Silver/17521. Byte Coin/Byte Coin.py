from sys import stdin

input = stdin.readline

N, W = map(int, input().split())

buy_price = int(input())
sell_price = buy_price
temp_gain = 0
for n in range(1, N):
    new_price = int(input())
    if new_price > sell_price:
        sell_price = new_price
        temp_gain = (W//buy_price) * (sell_price - buy_price)
    elif new_price < sell_price:
        if buy_price != sell_price:
            W += temp_gain
            temp_gain = 0
        buy_price = new_price
        sell_price = new_price

print(W+temp_gain)