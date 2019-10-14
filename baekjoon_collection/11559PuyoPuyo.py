from pprint import pprint

Puyo_map = []
for _ in range(12):
    Puyo_map.append(list(input()))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

def DFS(i, j, color):
    global cnt
    TF[i][j] = True
    cnt += 1
    coor_list.append([i,j])
    for k in range(4):
        idy = i + dy[k]
        jdx = j + dx[k]
        if 0 <= idy < 12 and 0 <= jdx < 6:
            if Puyo_map[idy][jdx] == color and TF[idy][jdx] == False:
                DFS(idy, jdx, color)

def downdown(i, j):
    if i == 11:
        return
    else:
        if Puyo_map[i + 1][j] == '.':
            Puyo_map[i + 1][j] = Puyo_map[i][j]
            Puyo_map[i][j] = '.'
            downdown(i + 1, j)
chain = 0
flag = True
while flag:
    flag = False
    TF = [ [False] * 6 for _ in range(12) ]
    cnt = 0
    for i in range(12):
        for j in range(6):
            if Puyo_map[i][j] != '.' and TF[i][j] == False:
                cnt = 0
                coor_list = []
                color = Puyo_map[i][j]
                DFS(i, j, color)
                if cnt >= 4:
                    flag = True
                    for coor in coor_list:
                        Puyo_map[coor[0]][coor[1]] = '.'

    if flag == True:
        chain += 1
    # pprint(Puyo_map)
    if flag == True:
        for i in range(10, -1, -1):
            # print(i)
            for j in range(6):
                if Puyo_map[i][j] != '.' and Puyo_map[i + 1][j] == '.':
                    downdown(i, j)
    # print('여기')
    # pprint(Puyo_map)

print(chain)