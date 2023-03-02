from sys import stdin

input = stdin.readline

real_answer = [*map(int, input().split())]
test_answer = []
point = []
total = 0
def pickone():
    global total, point

    if len(test_answer) < 10:
        for i in range(1,6):
            if len(test_answer) > 1 and test_answer[-1] == test_answer[-2] == i:
                continue

            point.append(real_answer[len(test_answer)] == i)
            test_answer.append(i)
            pickone()
            test_answer.pop()
            point.pop()
    else:
        total += sum(point) > 4
pickone()
print(total)