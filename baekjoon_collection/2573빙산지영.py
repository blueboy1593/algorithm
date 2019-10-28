# import sys
# sys.setrecursionlimit(10**6)

def melt(x, y):
    cnt=0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0<=new_x<N and 0<=new_y<M: #접근할 수 있다면,
            if arr[new_x][new_y] == 0:
                cnt+=1
    return cnt

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
            if visited[idy][jdx] == False and arr_2[idy][jdx] != 0:
                queue.append([idy, jdx])
                visited[idy][jdx] = True

# def DFS(x, y):
#     for k in range(4):
#         new_x = x + dx[k]
#         new_y = y + dy[k]
#         if visited[new_x][new_y]==False and arr_2[new_x][new_y] != 0:
#             visited[new_x][new_y]=True
#             DFS(new_x, new_y)

# if __name__=="__main__":
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_2=[[0]*M for _ in range(N)]
for i in range(N):
    arr_2[i] = arr[i][:]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans=0; flag=0

while True:
    flag = 0

    visited = [[False] * M for _ in range(N)]    
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and arr_2[i][j] != 0:
                start_x = i
                start_y = j
                # visited[i][j] = True
                # DFS(i, j)
                check_one_or_two(i, j)

                if flag ==1:
                    flag=2
                    break
                flag = 1
        if flag==2:
            break
    if flag==2:
        break

    for i in range(N):
        arr[i] = arr_2[i][:]
    flag2 = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                flag2 = 1
                # visited[i][j] = 1
                arr_2[i][j] -= melt(i, j)
                if arr_2[i][j] < 0:
                    arr_2[i][j]=0
    ans += 1
    if flag2 == 0:
        ans = 0
        break
print(ans)