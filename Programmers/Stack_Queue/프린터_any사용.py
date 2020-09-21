def solution(priorities, location):
    answer = 0
    new_priorities = [0] * len(priorities)
    for i, p in enumerate(priorities):
        if i == location:
            new_priorities[i] = (p, 1)
        else:
            new_priorities[i] = (p, 0)
    
    while True:
        a = new_priorities.pop(0)
        if any(a[0] < p[0] for p in new_priorities):
            new_priorities.append(a)
        else:
            answer += 1
            if a[1] == 1:
                return answer

solution([1, 1, 9, 1, 1, 1],0)