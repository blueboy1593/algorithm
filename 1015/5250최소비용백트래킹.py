from pprint import pprint
import sys
sys.stdin = open("5250_input.txt", "r")

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bikyo(a, b, c, d):
    ab = region_height[a][b]
    cd = region_height[c][d]
    if cd > ab:
        d = abs(ab - cd) + 1
    else:
        d = 1
    return d


def backtraking(i, j, cnt):
    global minmin
    if i == N - 1 and j == N - 1:
        if cnt < minmin:
            minmin = cnt
        return
    if cnt > minmin:
        return

    for k in range(4):
        idy = i + dy[k]
        jdx = j + dx[k]
        if 0 <= idy < N and 0 <= jdx < N:
            if visited[idy][jdx] == False:
                visited[idy][jdx] = True
                backtraking(idy, jdx, cnt + bikyo(i, j, idy, jdx))
                visited[idy][jdx] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    region_height = [0] * N
    for i in range(N):
        region_height[i] = list(map(int, input().split()))
    # pprint(region_height)
    visited = [ [False] * N for _ in range(N) ]

    start = (0, 0)
    visited[0][0] = True
    minmin = 99999999

    backtraking(0, 0, 0)
    print("#%d %d" %(tc, minmin))