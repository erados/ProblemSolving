from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
count = 0


def merge_sort(target):
    start = 0
    end = len(target) - 1

    if start < end:
        mid = int((start + end) / 2)
        target1 = merge_sort(target[start : mid + 1])
        target2 = merge_sort(target[mid + 1 : end + 1])

        target = merge(target1 + target2)
    return target


def merge(target):
    global K
    target.sort()
    if len(target) < K:
        K -= len(target)
        return target
    else:
        print(target[K - 1])
        exit()


merge_sort(arr)
print(-1)
