from sys import stdin

input = stdin.readline


class Node:
    now = None
    left = None
    right = None

    def __init__(self, now, left, right):
        self.now = now
        self.left = left
        self.right = right


nodes = [-1] * 26

N = int(input())
for n in range(N):
    now, left, right = map(lambda x: ord(x) - 65, input().split())
    nodes[now] = Node(now, left, right)


def preorder(now):
    ans = ""

    if now < 0:
        return ans

    ans += chr(now + 65) + preorder(nodes[now].left) + preorder(nodes[now].right)

    return ans


def inorder(now):
    ans = ""

    if now < 0:
        return ans

    ans += inorder(nodes[now].left) + chr(now + 65) + inorder(nodes[now].right)

    return ans


def postorder(now):
    ans = ""

    if now < 0:
        return ans

    ans += postorder(nodes[now].left) + postorder(nodes[now].right) + chr(now + 65)

    return ans


print(preorder(0))
print(inorder(0))
print(postorder(0))
