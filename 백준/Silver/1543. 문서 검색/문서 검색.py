from sys import stdin

input = stdin.readline

original = input().rstrip()
pattern = input().rstrip()


def create_table():
    # idx 에서 실패했을 때 갈 수 있는 idx 를 저장
    table = []
    idx = 0
    while idx < len(pattern):
        value = 0
        for i in range(idx):
            if pattern[:i] == pattern[idx - i : idx]:
                value = i
        table.append(value)
        idx += 1

    return table


def solve():
    global original
    table = create_table()
    original_idx = 0
    pattern_idx = 0
    answer = 0

    while original_idx < len(original):
        if pattern[pattern_idx] == original[original_idx]:
            pattern_idx += 1
            original_idx += 1

            if pattern_idx == len(pattern):
                pattern_idx = 0
                answer += 1

        elif pattern_idx > 0:
            pattern_idx = table[pattern_idx]
        else:
            original_idx += 1

    print(answer)


solve()


# ACBDACBE
# 00000123
