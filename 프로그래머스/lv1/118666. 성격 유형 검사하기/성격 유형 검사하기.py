def solution(survey, choices):
    answer = ""
    score_board = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0,
    }
    
    for i in range(len(survey)):
        types = survey[i]
        check = choices[i]
        if check > 3:
            score_board[types[1]] += check -4
        else:
            score_board[types[0]] += 4 - check 
        
    answer += 'R' if score_board['R'] >= score_board['T'] else 'T'
    answer += 'C' if score_board['C'] >= score_board['F'] else 'F'
    answer += 'J' if score_board['J'] >= score_board['M'] else 'M'
    answer += 'A' if score_board['A'] >= score_board['N'] else 'N'
    
    return answer