N, M = map(int, input().split())
tetromino = []
for _ in range(N):
    temp = list(map(int, input().split()))
    tetromino.append(temp)
visited = [ [ False ] * M for _ in range(N) ]
D = [(1, 0),(-1,0),(0,1),(0,-1)]
maxmax = 0

def tetris(i, j, cnt, temp_sum):
    global maxmax
    if cnt == 4:
        maxmax = max(maxmax, temp_sum)
        return
    else:
        for k in range(4):
            ny = i + D[k][0]
            nx = j + D[k][1]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == False:
                    value = tetromino[ny][nx]
                    visited[ny][nx] = True
                    tetris(ny, nx, cnt + 1, temp_sum + value)
                    visited[ny][nx] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        initial_sum = tetromino[i][j]
        tetris(i, j, 1, initial_sum)
        visited[i][j] = False

def bbaque(i, j, initial):
    global maxmax
    near = []
    for k in range(4):
        ny = i + D[k][0]
        nx = j + D[k][1]
        if 0 <= ny < N and 0 <= nx < M:
            near.append(tetromino[ny][nx])
    if len(near) == 3:
        temp_sum = initial + sum(near)
        maxmax = max(maxmax, temp_sum)
    elif len(near) == 4:
        near.sort()
        # print(near)
        near.pop(0)
        temp_sum = initial + sum(near)
        maxmax = max(maxmax, temp_sum)

for i in range(N):
    for j in range(M):
        initial = tetromino[i][j]
        bbaque(i, j, initial)

print(maxmax)