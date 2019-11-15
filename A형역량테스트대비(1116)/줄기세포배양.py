import sys
sys.stdin = open("줄기세포배양_input.txt", "r")
# import copy
from collections import deque

# copy 형식 바꿔보고 다시 해보기
# deque 로 바꿔서 다시 해보기
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    deactivation2 = deque()
    inactivation2 = deque()
    time = 0
    # 초기 상태 N + 2K 의 사이즈로 map 구성.
    cell_map = [ [0] * (M + 2*K) for _ in range(N + 2*K) ]
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(M):
            if temp[j] != 0:
                deactivation2.append([K + i, K + j, temp[j], temp[j]])
                cell_map[K + i][K + j] = 1
    # print(*cell_map, sep='\n')
    # print(deactivation2)
    # print('--------------------------------------------------------')

    while time < K:
        time += 1
        # print('시간은', time)
        leng = len(deactivation2)
        deactivation = deque([0] * leng)
        for i in range(leng):
            deactivation[i] = deactivation2[i][:]
        # deactivation = copy.deepcopy(deactivation2)
        deactivation2 = deque()
        # inactivation = copy.deepcopy(inactivation2)
        leng = len(inactivation2)
        inactivation = [0] * leng
        for i in range(leng):
            inactivation[i] = inactivation2[i][:]
        inactivation2 = []
        inactivation.sort(key=lambda x: x[2], reverse=True)
        while inactivation:
            inacti = inactivation.pop(0)
            y = inacti[0]
            x = inacti[1]
            value = inacti[2]
            for k in range(4):
                idy = y + D[k][0]
                jdx = x + D[k][1]
                if cell_map[idy][jdx] == 0:
                    cell_map[idy][jdx] = 1
                    deacti = [idy, jdx, value, value]
                    deactivation2.append(deacti)
            inacti[3] += 1
            if inacti[3] == inacti[2]:
                cell_map[y][x] = -1
            else:
                inactivation2.append(inacti)

        while deactivation:
            deacti = deactivation.popleft()
            deacti[3] -= 1
            if deacti[3] == 0:
                inacti = deacti[:]
                inactivation2.append(inacti)
            else:
                deactivation2.append(deacti)

        # print(inactivation2)
        # print(deactivation2)
        # print(*cell_map, sep='\n')
    result = len(inactivation2) + len(deactivation2)
    print("#%d %d" %(tc, result))