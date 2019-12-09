from copy import deepcopy
from pprint import pprint

N, M = map(int, input().split())
virus_map = []
for _ in range(N):
    temp = list(map(int, input().split()))
    virus_map.append(temp)
D = [(-1,0), (0, 1), (1, 0), (0, -1)]
min_time = 9999

# 맵 변경
base_comb = []
for i in range(N):
    for j in range(N):
        if virus_map[i][j] == 1:
            virus_map[i][j] = '-'
        if virus_map[i][j] == 2:
            virus_map[i][j] = '*'
            base_comb.append((i,j))

# 조합으로 M 개 뽑기
comb_list = []
virus_num = len(base_comb)
def make_comb(i, cnt, temp_list):
    if cnt == M:
        comb_list.append(temp_list)
        return
    for j in range(i + 1, virus_num):
        make_comb(j, cnt + 1, temp_list + [j])

# 여기 살짝 줄일 수 있을듯
for i in range(virus_num):
    make_comb(i, 1, [i])


# BFS 작업 함수
def do_BFS(queue):
    global min_time
    cnt = 0
    while queue:
        flag = False
        for i in range(N):
            for j in range(N):
                if copied_virus[i][j] == 0:
                    flag = True
        if flag == False:   
            break
        cnt += 1
        # 가지치기
        for _ in range(len(queue)):
            y, x = queue.pop(0)
            for k in range(4):
                idy = y + D[k][0]
                jdx = x + D[k][1]
                if 0 <= idy < N and 0 <= jdx < N:
                    if copied_virus[idy][jdx] == 0 or copied_virus[idy][jdx] == '*':
                        queue.append((idy, jdx))
                        copied_virus[idy][jdx] = cnt
    flag = False
    for i in range(N):
        for j in range(N):
            if copied_virus[i][j] == 0:
                flag = True
    if flag == False:
        if cnt < min_time:
            # print(cnt)
            # pprint(copied_virus)
            min_time = cnt

# 조합에서 돌려서 실행하기
for k in range(len(comb_list)):
    copied_virus = [0] * N
    for n in range(N):
        copied_virus[n] = virus_map[n][:]

    # pprint(copied_virus)
    # deque로 바꾸면 또 시간 절약될수도
    queue = []
    for l in range(M):
        queue.append(base_comb[comb_list[k][l]])
    for que in queue:
        copied_virus[que[0]][que[1]] = 1
    do_BFS(queue)

if min_time == 9999:
    min_time = -1
print(min_time)