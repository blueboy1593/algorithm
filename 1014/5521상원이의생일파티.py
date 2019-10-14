import sys
sys.stdin = open("5521_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    intimacy = [ [0] * (N + 1) for _ in range(N + 1) ]
    for _ in range(M):
        a, b = map(int, input().split())
        intimacy[a][b] = 1
        intimacy[b][a] = 1
    visited = [ False ] * (N + 1)
    visited[1] = True
    realfriend = []
    cometoparty = 0

    for j in range(2, N + 1):
        if intimacy[1][j] == 1:
            realfriend.append(j)
            visited[j] = True
    
    for real in realfriend:
        for k in range(2, N + 1):
            if intimacy[real][k] == 1 and visited[k] == False:
                visited[k] = True
    
    result = visited.count(True) - 1
    print("#%d %d" %(tc, result))