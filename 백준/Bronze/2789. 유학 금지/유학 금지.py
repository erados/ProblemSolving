w = input()

ans = ""
for c in w:
    if c not in "CAMBRIDGE":
        ans += c
print(ans)
