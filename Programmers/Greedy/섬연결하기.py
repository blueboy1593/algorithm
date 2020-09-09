# 이거 무조건 prim or cruskal 아니냐...

def solution(n, costs):
    visited = [ False ] * n
    costs.sort(key=lambda x: x[2])
    cost = costs.pop(0)
    visited[cost[0]] = True
    visited[cost[1]] = True
    answer = cost[2]

    while True:
        for cost in costs:
            a, b, price = cost
            if (visited[a] == True and visited[b] == False) or (visited[b] == True and visited[a] == False):
                answer += price
                visited[a] = True
                visited[b] = True
                costs.remove(cost)
                break
        if visited == [ True ] * n:
            break

    return answer

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])