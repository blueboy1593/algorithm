N = int(input())

color = []
for _ in range(N):
    color.append(list(input()))
D = [(1,0), (-1,0), (0,1), (0,-1)]


visited = [ [ False ] * N for _ in range(N) ]
visited2 = [ [ False ] * N for _ in range(N) ]

def cansee(i, j, munza):
    queue = [[i, j]]
    visited[i][j] = True
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for k in range(4):
            idy = y + D[k][0]
            jdx = x + D[k][1]
            if 0 <= idy < N and 0 <= jdx < N:
                if visited[idy][jdx] == False and color[idy][jdx] == munza:
                    visited[idy][jdx] = True
                    queue.append([idy, jdx])

def cannotseeRG(i, j):
    queue = [[i, j]]
    visited2[i][j] = True
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for k in range(4):
            idy = y + D[k][0]
            jdx = x + D[k][1]
            if 0 <= idy < N and 0 <= jdx < N:
                if visited2[idy][jdx] == False and (color[idy][jdx] == 'R' or color[idy][jdx] == 'G'):
                    visited2[idy][jdx] = True
                    queue.append([idy, jdx])

def cannotseeB(i, j):
    queue = [[i, j]]
    visited2[i][j] = True
    while queue:
        a = queue.pop(0)
        y = a[0]
        x = a[1]
        for k in range(4):
            idy = y + D[k][0]
            jdx = x + D[k][1]
            if 0 <= idy < N and 0 <= jdx < N:
                if visited2[idy][jdx] == False and color[idy][jdx] == 'B':
                    visited2[idy][jdx] = True
                    queue.append([idy, jdx])

cansee_cnt = 0
cannotsee_cnt = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            cansee(i, j, color[i][j])
            cansee_cnt += 1
        if visited2[i][j] == False:
            if color[i][j] == 'B':
                cannotseeB(i, j)
                cannotsee_cnt += 1
            else:
                cannotseeRG(i, j)
                cannotsee_cnt += 1

print(cansee_cnt)
print(cannotsee_cnt)