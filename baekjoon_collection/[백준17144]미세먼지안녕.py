R, C, T = map(int, input().split())
fine_dust = []
for _ in range(R):
    fine_dust.append(list(map(int, input().split())))
aircleaner = []
for i in range(R):
    for j in range(C):
        if fine_dust[i][j] == -1:
            aircleaner.append((i, j))

D = [(0,1), (0,-1), (1,0), (-1,0)]
def diffusion(i, j, dust):
    # dust = temp_fine_dust[i][j]
    some_dust = dust // 5
    dust_spreaded = 0
    for k in range(4):
        idy = i + D[k][0]
        jdx = j + D[k][1]
        if 0 <= idy < R and 0 <= jdx < C:
            if (idy, jdx) not in aircleaner:
                fine_dust[idy][jdx] += some_dust
                dust_spreaded += some_dust
    fine_dust[i][j] -= dust_spreaded

time = 0
while time < T:
    time += 1
    # 1단계 시작
    # deepcopy 중 혜준이에게 배운 가장 시간 짧은 방법 사용할 예정. 실패시 stack으로 바꾼다.
    # temp_fine_dust = [0] * R
    # for i in range(R):
    #     temp_fine_dust[i] = fine_dust[i][:]
    stack = []
    for i in range(R):
        for j in range(C):
            if fine_dust[i][j] > 0:
                stack.append((i, j, fine_dust[i][j]))

    for sta in stack:
        diffusion(sta[0], sta[1], sta[2])
    # print(*fine_dust, sep='\n')
    # 미세먼지 확산 끝
    # 2단계 시작 쉬움.
    y, x = aircleaner[0]
    fine_dust[y - 1][x] = 0
    for i in range(y - 1, 0, -1):
        fine_dust[i][0] = fine_dust[i - 1][0]
        fine_dust[i - 1][0] = 0
    for j in range(C - 1):
        fine_dust[0][j] = fine_dust[0][j + 1]
        fine_dust[0][j + 1] = 0
    for i in range(y):
        fine_dust[i][C - 1] = fine_dust[i + 1][C - 1]
        fine_dust[i + 1][C - 1] = 0
    for j in range(C - 1, 1, -1):
        fine_dust[y][j] = fine_dust[y][j - 1]
        fine_dust[y][j - 1] = 0

    y, x = aircleaner[1]
    fine_dust[y + 1][x] = 0
    for i in range(y + 1, R - 1):
        fine_dust[i][0] = fine_dust[i + 1][0]
        fine_dust[i + 1][0] = 0
    for j in range(C - 1):
        fine_dust[R - 1][j] = fine_dust[R - 1][j + 1]
        fine_dust[R - 1][j + 1] = 0
    for i in range(R - 1, y, -1):
        fine_dust[i][C - 1] = fine_dust[i - 1][C - 1]
        fine_dust[i - 1][C - 1] = 0
    for j in range(C - 1, 1, -1):
        fine_dust[y][j] = fine_dust[y][j - 1]
        fine_dust[y][j - 1] = 0
    # 쉬운게 아니라 겁나 복잡하네...
    # print(*fine_dust, sep='\n')
result = 0
for i in range(R):
    for j in range(C):
        result += fine_dust[i][j]

result += 2
print(result)