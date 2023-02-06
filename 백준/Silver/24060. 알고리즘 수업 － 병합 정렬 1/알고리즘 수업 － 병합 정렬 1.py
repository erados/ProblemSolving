from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
count = 0


def mergesort(p, r):
    if p < r:
        q = (p + r) // 2
        mergesort(p, q)
        mergesort(q + 1, r)
        merge(p, q, r)


def merge(p, q, r):
    global count
    temp = []
    i, j = p, q + 1
    while i <= q and j <= r:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= q:
        temp.append(arr[i])
        i += 1
    while j <= r:
        temp.append(arr[j])
        j += 1

    for i in range(r - p + 1):
        arr[p + i] = temp[i]
        count += 1
        if count == K:
            print(temp[i])
            exit()


mergesort(0, N - 1)
print(-1)
