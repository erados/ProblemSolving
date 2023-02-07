from math import sqrt

N = int(input())


def prime_checker(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for num in range(N, 2000001):
    if num == 1:
        continue
    str_num = str(num)
    if str_num == str_num[::-1] and prime_checker(num):
        print(num)
        break
