# from pprint import pprint
#
import sys
sys.stdin = open("5105_input.txt", "r")

T = int(input())

def findway(mapp, visited, i, j, N, self_cnt):
    global result
    visited[i][j]=True
    self_cnt += 1

    if mapp[i][j] == 3:
        if result > self_cnt:
            result = self_cnt
        return
    else:
        if 0 <= i+1 < N:
            if visited[i+1][j]==False and mapp[i+1][j] != 1:
                findway(mapp, visited, i+1, j, N, self_cnt)
        if 0 <= i - 1 < N:
            if visited[i-1][j] == False and mapp[i-1][j] != 1:
                findway(mapp, visited, i - 1, j, N, self_cnt)
        if 0 <= j + 1 < N:
            if visited[i][j+1] == False and mapp[i][j+1] != 1:
                findway(mapp, visited, i, j+1, N, self_cnt)
        if 0 <= j - 1 < N:
            if visited[i][j - 1] == False and mapp[i][j - 1] != 1:
                findway(mapp, visited, i, j - 1, N, self_cnt)


for tc in range(1, T+1):
    N = int(input())
    mapp = [ list(map(int, input())) for _ in range(N) ]
    self_cnt = 0
    result = 9999
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if mapp[i][j]==2:
                x=i
                y=j
                break

    findway(mapp, visited, x, y, N, self_cnt)
    if result == 9999:
        result = 0
    else:
        result -= 2
    print("#%d %s" % (tc, result))
