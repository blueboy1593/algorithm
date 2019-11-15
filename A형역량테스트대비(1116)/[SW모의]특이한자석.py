import sys
sys.stdin = open("특이한자석_input.txt", "r")
from collections import deque

def rotate_clock(arr):
    last = arr.pop()
    arr.appendleft(last)
    return arr


def rotate_reverse_clock(arr):
    first = arr.popleft()
    arr.append(first)
    return arr


def tobni_linked(tobni, rotation_direction):
    queue = deque([[tobni, rotation_direction]])
    linked = [[tobni, rotation_direction]]
    visited = [True] + [False] * 4
    visited[tobni] = True
    while queue:
        que = queue.popleft()
        queplus = que[0] + 1
        new_direction = - que[1]
        if 1 <= queplus <= 4 and visited[queplus] == False:
            if magnet_sawtooth[que[0]][2] != magnet_sawtooth[queplus][6]:
                queue.append([queplus, new_direction])
                visited[queplus] = True
                linked.append([queplus, new_direction])
        queminus = que[0] - 1
        if 1 <= queminus <= 4 and visited[queminus] == False:
            if magnet_sawtooth[que[0]][6] != magnet_sawtooth[queminus][2]:
                queue.append([queminus, new_direction])
                visited[queminus] = True
                linked.append([queminus, new_direction])
    return linked

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    magnet_sawtooth = [0]
    for _ in range(4):
        magnet_sawtooth.append(deque(list(map(int, input().split()))))
    rotation_info = []
    for _ in range(K):
        rotation_info.append(list(map(int, input().split())))
    result = 0

    for rotation in rotation_info:
        tobni = rotation[0]
        rotation_direction = rotation[1]
        needtochange = tobni_linked(tobni, rotation_direction)

        for j in range(len(needtochange)):
            tobni_num = needtochange[j][0]
            direc = needtochange[j][1]
            if direc == 1:
                magnet_sawtooth[tobni_num] = rotate_clock(magnet_sawtooth[tobni_num])
            elif direc == -1:
                magnet_sawtooth[tobni_num] = rotate_reverse_clock(magnet_sawtooth[tobni_num])


    for i in range(1, 5):
        result += magnet_sawtooth[i][0]*(2**(i-1))
    print("#%d %d" %(tc, result))