import sys
sys.stdin = open("1953_input.txt", "r")
from pprint import pprint

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
list1 = [1, 1, 1, 1]
list2 = [1, 1, 0, 0]
list3 = [0, 0, 1, 1]
list4 = [1, 0, 0, 1]
list5 = [0, 1, 0, 1]
list6 = [0, 1, 1 ,0]
list7 = [1, 0, 1, 0]

def make_double():
    for i in range(N):
        for j in range(M):
            a = jiha_map[i][j]
            if a != 0:
                double_map[2*i][2*j] = a
                visited[2*i][2*j] = 3
                make_tongro(2*i, 2*j, a)

def a_list(a):
    if a == 1:
        return list1
    if a == 2:
        return list2
    if a == 3:
        return list3
    if a == 4:
        return list4
    if a == 5:
        return list5
    if a == 6:
        return list6
    if a == 7:
        return list7

# 구분할 방법이 없네...
# 2배로 늘린 것과 좌표에서의 값.
def make_tongro(y, x, a):
    b = a_list(a)
    for i in range(4):
        if b[i] == 1:
            idy = y + dy[i]
            idx = x + dx[i]
            if 0 <= idy < 2*N and 0 <= idx < 2*M:
                double_map[idy][idx] -= 1
                if double_map[idy][idx] == -2:
                    visited[idy][idx] = 1
# 여기까지가 더블맵, visited 구현.


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    jiha_map = [ list(map(int, input().split())) for _ in range(N) ]

    # visited는 곧 통로가 될 것이다.
    visited = [ [0] * (2*M) for _ in range(2*N) ]
    double_map = [ [0] * (2*M) for _ in range(2*N) ]

    make_double()

    # 맵 메이킹 완료
    # BFS는 함수 바깥에서 해보자.
    start = [2*R, 2*C]
    queue = [start]
    cnt = 1
    result = 1
    while queue and cnt < L:
        cnt += 1
        for _ in range(len(queue)):
            a = queue.pop(0)
            y = a[0]
            x = a[1]
            for i in range(4):
                idy = y + dy[i]
                idx = x + dx[i]
                if 0 <= idy < 2 * N and 0 <= idx < 2 * M:
                    if visited[idy][idx] == 1:
                        visited[idy][idx] = 2
                        nidy = idy + dy[i]
                        nidx = idx + dx[i]
                        if visited[nidy][nidx] == 3:
                            visited[nidy][nidx] = 4
                            queue.append([nidy, nidx])
                            result += 1

    print("#%d %d" %(tc, result))