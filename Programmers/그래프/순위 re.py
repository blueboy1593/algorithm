def solution(n, results):
    answer = 0

    front = [ set() for _ in range(n + 1) ]
    back = [ set() for _ in range(n + 1) ]
    for a, b in results:
        front[b].add(a)
        back[a].add(b)

    for i in range(1, n + 1):
        for a in back[i]: front[a].update(front[i])
        for b in front[i]: back[b].update(back[i])

    for i in range(1, n + 1):
        if len(front[i]) + len(back[i]) == n - 1:
            answer += 1
    print(answer)
    return answer


# solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
solution(8, [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [2, 7]])