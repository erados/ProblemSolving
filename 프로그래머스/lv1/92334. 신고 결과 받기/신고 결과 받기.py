
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    name_to_num = {k: v for v, k in enumerate(id_list)}
    graph = [[False] * len(id_list) for i in range(len(id_list))]

    for item in report:
        a, b = (name_to_num[k] for k in item.split())
        graph[b][a] = True

    for b in graph:
        if sum(b) >= k:
            for index, value in enumerate(b):
                if value:
                    answer[index] += 1


    return answer