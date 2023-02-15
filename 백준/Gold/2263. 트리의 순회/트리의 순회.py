from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

N = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

ans = []
inorder_map = [0] * (N + 1)

for i in range(N):
    inorder_map[inorder[i]] = i


def solve(ps, pe, ins, ine):
    if ps > pe or ins > ine:
        return

    # 1. postorder 에서 root 를 찾는다
    root = postorder[pe]

    # 2. inorder 에서 root 를 찾아 오른쪽 왼쪽으로 나눈다.
    root_index = inorder_map[root]

    left_nodes = root_index - ins

    # 3. postorder 에서 왼쪽에만 포함된 내용을 찾아 1~3을 반복한다.
    ans.append(root)
    solve(ps, ps + left_nodes - 1, ins, root_index - 1)
    solve(ps + left_nodes, pe - 1, root_index + 1, ine)

    return


solve(0, N - 1, 0, N - 1)
print(*ans)
