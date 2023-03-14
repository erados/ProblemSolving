from sys import stdin

input = stdin.readline

N = int(input())
M = int(input())

votes = map(int, input().split())

candidate_vote = {}

for idx, candidate in enumerate(votes):
    if N <= len(candidate_vote) and candidate not in candidate_vote:
        temp = sorted(candidate_vote.items(), key=lambda x: (-x[1][0], -x[1][1]))
        del candidate_vote[temp[-1][0]]

    if candidate not in candidate_vote:
        candidate_vote[candidate] = [0, idx]
    candidate_vote[candidate][0] += 1

print(*sorted(candidate_vote))
