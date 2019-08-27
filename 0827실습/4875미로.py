import sys
sys.stdin=open("4875_input.txt", "r")

def findway(mapp, visited, i, j, N):
    global re
    visited[i][j]=True
    if mapp[i][j] == 3:
        re = True
        return True
    else:
        if 0 <= i+1 < N:
            if visited[i+1][j]==False and mapp[i+1][j] != 1:
                findway(mapp, visited, i+1, j, N)
        if 0 <= i - 1 < N:
            if visited[i-1][j] == False and mapp[i-1][j] != 1:
                findway(mapp, visited, i - 1, j, N)
        if 0 <= j + 1 < N:
            if visited[i][j+1] == False and mapp[i][j+1] != 1:
                findway(mapp, visited, i, j+1, N)
        if 0 <= j - 1 < N:
            if visited[i][j - 1] == False and mapp[i][j - 1] != 1:
                findway(mapp, visited, i, j - 1, N)

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    mapp = []
    visited = [ [False]*N for _ in range(N)]
    re = False

    for i in range(N):
        temp=list(map(int,input()))
        mapp.append(temp)

    for i in range(N):
        for j in range(N):
            if mapp[i][j]==2:
                x=i
                y=j
                break

    findway(mapp, visited, x, y, N)
    print("#%d %d" %(tc,re))


# def findway(mapp, visited, i, j):
#     try:
#         visited[i][j]=True
#         if mapp[i][j]==3:
#             return True
#
#
#         if visited[i+1][j]==False and mapp[i+1][j]==0:
#             findway(mapp, visited, i+1, j)
#         if visited[i-1][j] == False and mapp[i-1][j] == 0:
#             findway(mapp, visited, i - 1, j)
#         if visited[i][j+1] == False and mapp[i][j+1] == 0:
#             findway(mapp, visited, i, j+1)
#         if visited[i][j - 1] == False and mapp[i][j - 1] == 0:
#             findway(mapp, visited, i, j - 1)
#     except IndexError:
#         pass