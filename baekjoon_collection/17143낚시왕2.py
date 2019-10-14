from pprint import pprint

R, C, M = map(int, input().split())
shark_info = [ [0] * (C + 1) for _ in range(R + 1) ]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark_info[r][c] = [s, d, z]
man = 0
fished_shark = 0
D = [0, (-1, 0), (1, 0), (0, 1), (0, -1)]

def updown(i, j, temp_info):
    s = temp_info[0] % ((R - 1) * 2)
    d = temp_info[1]
    while s > 0:
        i = i + D[d][0]
        if i == 1:
            d = 2
        if i == R:
            d = 1
        s -= 1
    return (i, j)

def leftright(i, j, temp_info):
    s = temp_info[0] % ((C - 1) * 2)
    d = temp_info[1]
    while s > 0:
        j = j + D[d][1]
        if j == 1:
            d = 3
        if j == C:
            d = 4
        s -= 1
    return (i, j)

while man < C + 1:
    man += 1
    for k in range(R + 1):
        if shark_info[k][man] != 0:
            fished_shark += shark_info[k][man][2]
            shark_info[k][man] = 0
            break
    
    new_shark_info = [ [0] * (C + 1) for _ in range(R + 1) ]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            temp_info = shark_info[i][j]
            if temp_info != 0:
                if temp_info[1] == 1 or temp_info[1] == 2:
                    a = updown(i, j, temp_info)
                    print(a)
                    if new_shark_info[a[0]][a[1]] != 0:
                        if new_shark_info[a[0]][a[1]][2] < temp_info[2]:
                            new_shark_info[a[0]][a[1]] = temp_info
                    else:        
                        new_shark_info[a[0]][a[1]] = temp_info
                if temp_info[1] == 3 or temp_info[1] == 4:
                    b = leftright(i, j, temp_info)
                    if new_shark_info[b[0]][b[1]] != 0:
                        if new_shark_info[b[0]][b[1]][2] < temp_info[2]:
                            new_shark_info[b[0]][b[1]] = temp_info
                    else:
                        new_shark_info[b[0]][b[1]] = temp_info
    shark_info = new_shark_info
pprint(shark_info)
pprint(new_shark_info)