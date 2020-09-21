def solution(priorities, location):
    answer = 0
    target_number = priorities[location]
    target_cnt = 0
    for i, p in enumerate(priorities):
        if p == target_number:
            target_cnt += 1
        if i == location:
            # 몇번째인지
            target_loc = target_cnt
            break
    priorities.sort(reverse=True)
    turn = priorities.index(target_number)
    answer = turn + target_loc - 1
    return answer

solution([1, 1, 9, 1, 1, 1],0)