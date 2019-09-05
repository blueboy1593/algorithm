import itertools
result = 99999

def for_short(chicken):
    global cnt, result
    for one in one_list:
        one[2] = 200
    for y in range(N):
        for x in range(N):
            if chicken[y][x] == 2:
                for one in one_list:
                    i = one[0]
                    j = one[1]
                    temp_dis = abs(y-i) + abs(x - j)
                    if temp_dis < one[2]:
                        one[2] = temp_dis
    cnt = 0
    for one in one_list:
        cnt += one[2]
    
    if cnt < result:
        result = cnt

N, M = map(int, input().split())
original_chicken = []
for _ in range(N):
    temp = list(map(int, input().split()))
    original_chicken.append(temp)
chicken_list = []
one_list = []
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for i in range(N):
    for j in range(N):
        if original_chicken[i][j] == 2:
            chicken_list.append([i, j])
            original_chicken[i][j] = 0
        if original_chicken[i][j] == 1:
            one_list.append([i, j])
for one in one_list:
    one.append(200)

johab = list(itertools.combinations(chicken_list, M))

c_leng = len(chicken_list)
for jo in johab:
    cnt = 0
    chicken = []
    for k in range(N):
        temp = original_chicken[k][:]
        chicken.append(temp)

    for i in range(M):
        chic = jo[i]
        y = chic[0]
        x = chic[1]
        chicken[y][x] = 2

    for_short(chicken)

print(result)
