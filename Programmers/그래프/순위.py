def solution(n, results):
    answer = 0
    if n == 1:
        return 1

    front = [ set() for _ in range(n + 1) ]
    back = [ set() for _ in range(n + 1) ]
    for res in results:
        a, b = res
        # 1번 로직. b의 앞에 a를 추가
        front[b].add(a)
        # 2번 로직. b의 뒤에 있는 요소들의 앞에 a를 추가
        # 3번 로직. b의 뒤에 있는 요소들을 a의 뒤에 추가
        if back[b]:
            for bb in back[b]:
                front[bb].add(a)
                back[a].add(bb)
                
        back[a].add(b)
        if front[a]:
            for aa in front[a]:
                back[aa].add(b)
                front[b].add(aa)
    # print(front, back)
    
    for i in range(1, n + 1):
        if len(front[i]) + len(back[i]) == n - 1:
            answer += 1
    print(front, back)
    print(answer)
    return answer


# solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
solution(8, [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [2, 7]])