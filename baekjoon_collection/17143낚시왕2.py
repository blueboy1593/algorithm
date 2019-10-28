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
    if i == 1:
        d = 2
    if i == R:
        d = 1
    while s > 0:
        i = i + D[d][0]
        if i == 1:
            d = 2
        if i == R:
            d = 1
        s -= 1
    temp_info[1] = d
    if new_shark_info[i][j] != 0:
        if new_shark_info[i][j][2] < temp_info[2]:
            new_shark_info[i][j] = temp_info
    else:        
        new_shark_info[i][j] = temp_info
    return

def leftright(i, j, temp_info):
    s = temp_info[0] % ((C - 1) * 2)
    d = temp_info[1]
    if j == 1:
        d = 3
    if j == C:
        d = 4
    while s > 0:
        j = j + D[d][1]
        if j == 1:
            d = 3
        if j == C:
            d = 4
        s -= 1
    temp_info[1] = d
    if new_shark_info[i][j] != 0:
        if new_shark_info[i][j][2] < temp_info[2]:
            new_shark_info[i][j] = temp_info
    else:
        new_shark_info[i][j] = temp_info
    return

while man < C:
    man += 1
    for k in range(1, R + 1):
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
                    updown(i, j, temp_info)
                if temp_info[1] == 3 or temp_info[1] == 4:
                    leftright(i, j, temp_info)                
    shark_info = new_shark_info

print(fished_shark)