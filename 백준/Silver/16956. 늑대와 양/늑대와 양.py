from sys import stdin


input = stdin.readline

R, C = map(int, input().split())
graph = [input()[:-1] for r in range(R)]


for r in graph:
    if "SW" in r or "WS" in r:
        print(0)
        exit()

for c in map(lambda x: "".join(x), zip(*graph)):
    if "SW" in c or "WS" in c:
        print(0)
        exit()


print(1)
for r in graph:
    print(r.replace(".", "D"))
