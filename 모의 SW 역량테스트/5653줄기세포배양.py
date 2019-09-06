from pprint import pprint
import sys
sys.stdin = open("5653_input.txt", "r")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def make_stemcell():
    for i in range(N):
        for j in range(M):
            a = chogi_cell[i][j]
            if a != 0:
                ini = a + 1
                stem_cell[k + i][k + j] = [i, j, 0, ini, ini]


def BFS_cell(i, j):
    global cnt
    a = stem_cell[i][j]
    print(a)
    queue = [a]
    while queue:
        for i in range(len(queue)):
            print(queue[i])
            b = queue[i]
            y = b[0]
            x = b[1]
            stem_cell[y][x][4] -= 1
            ini = b[3]
            tl = stem_cell[y][x][4]
            visited[y][x] = True
            if tl == 1:
                for j in range(4):
                    idy = y + dy[j]
                    idx = x + dx[j]
                    if visited[idy][idx] == False:
                        stem = stem_cell[idy][idx]
                        if stem == 0:
                            stem_cell[idy][idx] = [idy, idx, cnt, ini, ini]
                            queue.append(stem_cell[idy][idx])
                        elif stem[2] == cnt:
                            if stem[3] < ini:
                                stem_cell[idy][idx] = [idy, idx, cnt, ini, ini]
                                for l in range(len(queue)):
                                    if queue[l][0] == idy and queue[l][1] == idx:
                                        queue[l] = [idy, idx, cnt, ini, ini]
                        elif stem[2] < cnt:
                            pass
        for




T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    k = K + 1
    chogi_cell = [ list(map(int, input().split())) for _ in range(N) ]
    stem_cell = [ [0] * (M + 2*K) for _ in range(N + 2*K) ]
    visited = [ [False] * (M + 2*K) for _ in range(N + 2*K) ]
    # cnt는 중요한 역할이다 여기서.
    cnt = 0

    make_stemcell()
    while cnt <= K:
        cnt += 1
        for i in range(k - cnt, k + N + cnt):
            for j in range(k - cnt, k + M + cnt):
                if stem_cell[i][j] != 0:
                    print(stem_cell[i][j])
                    BFS_cell(i, j)

    # while에서 나와서 활성화된 숫자 세기!!!




    pprint(stem_cell)