from heapq import heappop, heappush

def solution(n, m, puddles):
    answer = 0
    road_map = [ [ 0 ] * n for _ in range(m) ]
    for puddle in puddles:
        road_map[puddle[1] - 1][puddle[0] - 1] = 1
    visited = [ [ (float('inf'), 1) ] * n for _ in range(m) ]
    print(*road_map, sep='\n')
    print(*visited, sep='\n')

    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    heap_stack = []
    # [최단거리, i, j]
    heappush(heap_stack, [0, 0, 0])
    while heap_stack:
        print(heap_stack)
        a = heappop(heap_stack)
        dis, i, j = a
        for k in range(4):
            idy = i + D[k][0]
            jdx = j + D[k][1]
            if 0 <= idy < m and 0 <= jdx < n:
                if road_map[idy][jdx] == 0:
                    if dis + 1 < visited[idy][jdx][0]:
                        visited[idy][jdx] = (dis + 1, visited[i][j][1])
                        heappush(heap_stack, [dis + 1, idy, jdx])
                    elif dis + 1 == visited[idy][jdx][0]:
                        visited[idy][jdx] = (dis + 1, visited[idy][jdx][1] + visited[i][j][1])
    # print(visited)
    if visited[m-1][n-1][0] == float('inf'):
        return 0
    answer = visited[m-1][n-1][1] % 1000000007
    print(answer)
    print(*visited, sep='\n')
    
    return answer

solution(4,3,[[2, 2]])
solution(4,3,[[1,2],[2, 2]])