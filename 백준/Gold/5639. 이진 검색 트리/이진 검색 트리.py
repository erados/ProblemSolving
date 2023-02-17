from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)
input = stdin.readline

stack = []


def postorder(start, end):
    root = stack[start]
    if start == end:
        print(root)
        return

    if root > stack[end] or root < stack[start + 1]:
        postorder(start + 1, end)
        print(root)
        return

    mid = end
    for i in range(1, end - start + 1):
        if root < stack[start + i]:
            mid = start + i - 1
            break
    if start < mid:
        postorder(start + 1, mid)
    if mid < end:
        postorder(mid + 1, end)
    print(root)


while True:
    try:
        a = int(input())
        stack.append(a)
    except Exception:
        postorder(0, len(stack) - 1)
        exit()
