import sys
sys.stdin = open("5188_input.txt", "r")

dx = [1, 0]
dy = [0, 1]

def start_find(i, j, cnt):
    global minmin
    cnt += choisohab[i][j]
    if i == N - 1 and j == N -1:
        if cnt < minmin:
            minmin = cnt
        return
    else:
        for k in range(2):
            id = i + dx[k]
            jd = j + dy[k]
            if 0 <= id < N and 0 <= jd < N:
                start_find(id, jd, cnt)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    choisohab = []
    for _ in range(N):
        choisohab.append(list(map(int, input().split())))
    minmin = 99999999

    start_find(0, 0, 0)

    print("#%d %d" %(tc, minmin))