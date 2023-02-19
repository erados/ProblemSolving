def solution(s):
    answer = []
    cheat_sheet = {
        'zer':('0',4),
        'one':('1',3),
        'two':('2',3),
        'thr':('3',5),
        'fou':('4',4),
        'fiv':('5',4),
        'six':('6',3),
        'sev':('7',5),
        'eig':('8',5),
        'nin':('9',4),
    }
    i = 0
    while i < len(s):
        if s[i].isdigit():
            answer.append(s[i])
            i+=1
            continue
        num, l = cheat_sheet[s[i:i+3]]
        i += l
        answer.append(num)
    return int("".join(answer))