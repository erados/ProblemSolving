from sys import stdin

input = stdin.readline

N = int(input())
switches = list(map(int, input().split()))
cheat_sheet = [1, 0]
M = int(input())
for m in range(M):
    gender, number = map(int, input().split())
    number = number - 1
    if gender == 1:
        temp = number
        while temp < N:
            switches[temp] = cheat_sheet[switches[temp]]
            temp += number + 1
    else:
        right = number + 1
        left = number - 1
        while right < N and left >= 0 and switches[left] == switches[right]:
            switches[left] = cheat_sheet[switches[left]]
            switches[right] = cheat_sheet[switches[right]]
            left -= 1
            right += 1
        switches[number] = cheat_sheet[switches[number]]

i = 0
while i < N:
    print(*switches[i:i+20])
    i += 20
        
