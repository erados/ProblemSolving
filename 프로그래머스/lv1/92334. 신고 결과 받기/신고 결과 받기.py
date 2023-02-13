from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    name_to_num = {name : index for index, name in enumerate(id_list)}
    graph = defaultdict(set)
    
    for item in report:
        a, b = item.split()
        graph[b].add(a)
    for b in graph:
        if len(graph[b]) >= k:
            for a in graph[b]:
                answer[name_to_num[a]] += 1
    
    
    return answer