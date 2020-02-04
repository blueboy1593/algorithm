N, M, D = map(int, input().split())
copyenemies = []
for _ in range(N):
    copyenemies.append(list(map(int, input().split())))

arrangement_list = []
for i in range(M):
    for j in range(i + 1, M):
        for k in range(j + 1, M):
            arrangement_list.append([i, j, k])
# print(*arrangement_list, sep='\n')

def attack(archer, n):
    global kill_point
    dis = 1
    killing = 0
    while dis <= D:
        for d in range(-(dis - 1), dis):
            if 0 <= archer + d < M and n - (dis-abs(d)) >= 0:
                if enemies[n - (dis-abs(d))][archer + d] == 1:
                    killing = (n - (dis-abs(d)), archer + d)
                    if killing not in killed_enemy:
                        killed_enemy.append(killing)
                        kill_point += 1
                    break
        if killing != 0:
            break
        dis += 1

max_killed = 0

for arrange in arrangement_list:
    # 각각의 경우의 수 시작!
    enemies = [0] * N
    for i in range(N):
        enemies[i] = copyenemies[i][:]

    kill_point = 0
    n = N
    while n > 0:
        killed_enemy = []
        for archer in arrange:
            # 이건 3회 시행한다.
            attack(archer, n)
        for killing in killed_enemy:
            a, b = killing
            enemies[a][b] = 0
        n -= 1
    if kill_point > max_killed:
        max_killed = kill_point
    # if kill_point == 6:
        # print(arrange)

print(max_killed)