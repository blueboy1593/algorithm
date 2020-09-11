from collections import deque

def solution(n, edge):
    answer = 0
    visited = [ [0] * (n + 1) for _ in range(n + 1) ]
    for e in edge:
        visited[e[0]][e[1]] = 1
        visited[e[1]][e[0]] = 1
    visited_node = [False] * (n + 1)
    visited_node[1] = True
    cnt = 0

    queue = deque([1])
    while queue:
        answer = cnt
        cnt = 0
        for _ in range(len(queue)):
            q = queue.popleft()
            for j in range(1, n + 1): # 여기가 시간이 많이걸리네
                if visited[q][j] == 1:
                    if visited_node[j] == False:
                        visited_node[j] = True
                        queue.append(j)
                        cnt += 1
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])