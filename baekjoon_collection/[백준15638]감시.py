from pprint import pprint

N, M = map(int, input().split())
office = []
for _ in range(N):
    office.append(list(map(int, input().split())))
result = 99999999

base = []
five_list = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 4:
            base.append((office[i][j], i, j))
        elif office[i][j] == 5:
            five_list.append((i, j))
# print(base)

comb_list = []
L = len(base)
# 1번 중복 조합 만들어야지.
def make_duplication(i, arr, cnt):
    if cnt == L:
        comb_list.append(arr[:])
        return
    if base[i][0] == 2:
        for j in range(2):
            make_duplication(i + 1, arr + [j], cnt + 1)
    else:
        for j in range(4):
            make_duplication(i + 1, arr + [j], cnt + 1)
# 함수 밖 만드는 코드
if base != []:
    if base[0][0] == 2:
        for j in range(2):
            make_duplication(1, [j], 1)
    if base[0][0] != 2:
        for j in range(4):
            make_duplication(1, [j], 1)
    # 하아... 기가 막히기는 한데........ 디버깅.........ㅎ
# print(comb_list)
# 중복 조합 짠거 기가 막히다... 실력이 늘기는 느는구나.
# 앞으로는 방법은 정형화 되어있으니까 아마 내가 하는만큼 늘거야 강현아.

# 번외. 5가 포함되었을 경우.
for five in five_list:
    y = five[0]
    x = five[1]
    D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 이것도 가끔 쓰는 스킬이지.
    # 스킬은 좋은데 속도가 걱정됨.
    for k in range(4):
        yy = y
        xx = x
        while True:
            yy = yy + D[k][0]
            xx = xx + D[k][1]
            if not (0 <= yy < N and 0 <= xx < M):
                break
            if office[yy][xx] == 6:
                break
            if office[yy][xx] == 0:
                office[yy][xx] = '#'
# pprint(office)
# 잘 작동 한다.

# 2번 state에 따른 시야 처리 함수
def CCTV(way, z, y, x):
    D = [(0,1), (1,0), (0,-1), (-1,0)]
    if z == 1:
        while True:
            y = y + D[way][0]
            x = x + D[way][1]
            if not (0 <= y < N and 0 <= x < M):
                break
            if copied_office[y][x] == 6:
                break
            if copied_office[y][x] == 0:
                copied_office[y][x] = '#'
    if z == 2:
        for k in range(4):
            if k % 2 == way:
                yy = y
                xx = x
                while True:
                    yy = yy + D[k][0]
                    xx = xx + D[k][1]
                    if not (0 <= yy < N and 0 <= xx < M):
                        break
                    if copied_office[yy][xx] == 6:
                        break
                    if copied_office[yy][xx] == 0:
                        copied_office[yy][xx] = '#'
    if z == 3:
        # k 또 써도 됨!
        for k in range(2):
            yy = y
            xx = x
            kk = (way + k) % 4
            while True:
                yy = yy + D[kk][0]
                xx = xx + D[kk][1]
                if not (0 <= yy < N and 0 <= xx < M):
                    break
                if copied_office[yy][xx] == 6:
                    break
                if copied_office[yy][xx] == 0:
                    copied_office[yy][xx] = '#'
    if z == 4:
        for k in range(4):
            # 하나만 아니면 되니깐
            if k != way:
                yy = y
                xx = x
                while True:
                    yy = yy + D[k][0]
                    xx = xx + D[k][1]
                    if not (0 <= yy < N and 0 <= xx < M):
                        break
                    if copied_office[yy][xx] == 6:
                        break
                    if copied_office[yy][xx] == 0:
                        copied_office[yy][xx] = '#'

# 최종 처리 로직
for comb in comb_list:
    dead_zone = 0
    copied_office = [0] * N
    for i in range(N):
        copied_office[i] = office[i][:]

    for s in range(L):
        z = base[s][0]
        y = base[s][1]
        x = base[s][2]
        CCTV(comb[s], z, y, x)

    # 사각지대 세고 최소랑 비교.
    for i in range(N):
        for j in range(M):
            if copied_office[i][j] == 0:
                dead_zone += 1
    result = min(result, dead_zone)

if result == 99999999:
    result = 0
    for i in range(N):
        for j in range(M):
            if office[i][j] == 0:
                result += 1

print(result)