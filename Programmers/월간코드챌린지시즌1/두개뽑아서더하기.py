from itertools import combinations

def solution(numbers):
    answer = set()
    combs = combinations(numbers, 2)
    for comb1, comb2 in combs:
        answer.add(comb1 + comb2)
    answer = list(answer)
    answer.sort()
    return answer

solution([2,1,3,4,1])