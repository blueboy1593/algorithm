def solution(n, results):
    answer = 0
    INF = int(1e9)

    m = len(results)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    for i, j in results:
        graph[i][j] = 1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for i in range(1, n+1):
        flag = 0
        for j in range(1, n+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                flag += 1
        if flag == n:
            answer += 1
    print(answer)
    return answer

solution(8, [[1, 2], [2, 3], [2, 7], [3, 4], [5, 6], [6, 7], [7, 8]])