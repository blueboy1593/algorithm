from collections import defaultdict

def solution(t):
    answer = [0]
    injub = defaultdict(list)
    for a, b in t:
        injub[a].append(b)
        injub[b].append(a)
    
    def backtracking(node, cnt):
        if cnt > answer[0]:
            answer[0] = cnt
        
        node_injub = injub[node]
        for no in node_injub:
            if visited[no] == 0:
                visited[no] += 1
                backtracking(no, cnt + 1)
                visited[no] -= 1
            elif visited[no] == 1:
                visited[no] += 1
                backtracking(no, cnt)
                visited[no] -= 1

    for key in injub.keys():
        visited = defaultdict(int)
        visited[key] += 1
        backtracking(key, 1)
    return answer[0]
    
solution([[5,1],[2,5],[3,5],[3,6],[2,4],[4,0]])
# solution([[2,5],[2,0],[3,2],[4,2],[2,1]])