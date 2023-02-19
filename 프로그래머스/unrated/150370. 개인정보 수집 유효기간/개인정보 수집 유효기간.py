def solution(today, terms, privacies):
    answer = []
    today = [*map(int,today.split('.'))]
    terms ={k: int(v) for k, v in [term.split() for term in terms]}

    i = 1
    for priv in privacies:
        date, term =  priv.split(' ')
        date = [*map(int,date.split("."))]
        print((today[0] - date[0]) * 12 + (today[1] - date[1]) + (today[2] >= date[2]), terms[term])
        if (today[0] - date[0]) * 12 + (today[1] - date[1])  + (today[2] >= date[2]) > terms[term]:
            answer.append(i)
        
        i += 1
    return answer