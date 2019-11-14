N, M = map(int, input().split())
bluestorm = []
for _ in range(N):
    bluestorm.append(list(map(int, input().split())))
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def numbering_sum(i, j, number):
    queue = [(i, j)]
    bluestorm[i][j] = number
    while queue:
        que = queue.pop(0)
        y, x = que
        for dy, dx in D:
            idy = y + dy
            jdx = x + dx
            if 0 <= idy < N and 0 <= jdx < M:
                if bluestorm[idy][jdx] == 1:
                    bluestorm[idy][jdx] = number
                    queue.append((idy, jdx))

# 1번 섬 구분하기.
number = 2
for i in range(N):
    for j in range(M):
        if bluestorm[i][j] == 1:
            numbering_sum(i, j, number)
            number += 1
# print(*bluestorm, sep='\n')

# 2번 섬 간의 인접 리스트 만들기 포문
# 이거 근데 이따가 다른 애들 어떻게 했는지 한번 확인해보자.
num_of_sum = number
injub_sum = [ [101] * num_of_sum for _ in range(num_of_sum) ]

# 가로
for i in range(N):
    temp_island = 0
    temp_bridge = 0
    for j in range(M):
        if bluestorm[i][j] != 0:
            if temp_island == 0:
                temp_island = bluestorm[i][j]
                continue
            elif temp_bridge >= 2:
                a = temp_island
                b = bluestorm[i][j]
                if temp_bridge < injub_sum[a][b]:
                    injub_sum[a][b] = temp_bridge
                    injub_sum[b][a] = temp_bridge
                temp_bridge = 0
                temp_island = b
            else:
                temp_island = bluestorm[i][j]
                temp_bridge = 0
        # 0일 때
        else:
            if temp_island:
                temp_bridge += 1

for j in range(M):
    temp_island = 0
    temp_bridge = 0
    for i in range(N):
        if bluestorm[i][j] != 0:
            if temp_island == 0:
                temp_island = bluestorm[i][j]
                continue
            elif temp_bridge >= 2:
                a = temp_island
                b = bluestorm[i][j]
                if temp_bridge < injub_sum[a][b]:
                    injub_sum[a][b] = temp_bridge
                    injub_sum[b][a] = temp_bridge
                temp_bridge = 0
                temp_island = b
            else:
                temp_island = bluestorm[i][j]
                temp_bridge = 0
        # 0일 때
        else:
            if temp_island:
                temp_bridge += 1
# print(*injub_sum, sep='\n')

def prim(num):
    node_list = [num]
    go_possible = []
    total_length = 0
    for j in range(2, num_of_sum):
        if injub_sum[num][j] != 101:
            go_possible.append([j, injub_sum[num][j]])
    while go_possible:
        if len(node_list) == num_of_sum - 2:
            break
        go_possible.sort(key=lambda x: x[1])
        # print(go_possible)

        # 섬을 미처 다 잇지 못하는 경우가 생기기에 flag를 써줘야하지.
        flag = False
        for go in go_possible:
            if go[0] not in node_list:
                flag = True
                node_list.append(go[0])
                total_length += go[1]
                for j in range(2, num_of_sum):
                    if injub_sum[go[0]][j] != 101:
                        if j not in node_list:
                            go_possible.append([j, injub_sum[go[0]][j]])
                break
        if flag == False:
            return -1
        # print(node_list)
    return total_length

# 3번 프림 알고리즘 or 크루스칼 알고리즘 적용
# 프림 적용해보자.
result = prim(2)

# 이거 안해준거 개빡치네 생각해보닊깐
if result == 0:
    result = -1
print(result)