N, M = map(int, input().split())

bingsan = list()
for _ in range(N):
    bingsan.append(list(map(int, input().split())))


D = [(1,0), (-1,0), (0,1), (0,-1)]

def check_one_or_two(i, j):
    queue = [[i, j]]
    visited[i][j] = True
    while queue:
        a = queue.pop(0)
        for k in range(4):
            idy = a[0] + D[k][0]
            jdx = a[1] + D[k][1]
            # 인덱스 에러 날 수 있음 여기서.
            if visited[idy][jdx] == False and bingsan[idy][jdx] != 0:
                queue.append([idy, jdx])
                visited[idy][jdx] = True
            if bingsan[idy][jdx] == 0:
                bingsan[a[0]][a[1]] -= 1
        if bingsan[a[0]][a[1]] <= 0:
            bingsan[a[0]][a[1]] = -1
# def melt(i, j):
#     for k in range(4):
#         idy = i + D[k][0]
#         jdx = j + D[k][1]
#         if bingsan[idy][jdx] == 0:
#             bingsan[i][j] -= 1
#     if bingsan[i][j] <= 0:
#         bingsan[i][j] = -1


cnt = 0
while True:
    flag = False
    visited = [ [False] * M for _ in range(N) ]
    checkcheck = 0
    for i in range(N):
        for j in range(M):
            if bingsan[i][j] != 0 and visited[i][j] == False:
                checkcheck += 1
                if checkcheck > 1:
                    result = cnt
                    break
                check_one_or_two(i, j)
                flag = True
        if checkcheck > 1:
            break
    if checkcheck > 1:
        break
    cnt += 1

    if flag == False:
        cnt = 0
        break
    # for i in range(N):
    #     for j in range(M):
    #         if bingsan[i][j] != 0:
    #             melt(i, j)
    
    for i in range(N):
        for j in range(M):
            if bingsan[i][j] == -1:
                bingsan[i][j] = 0

print(cnt)