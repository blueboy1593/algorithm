n, m = map(int, input().split())
def make_bitway(num):
    temp = [0, 0, 0, 0]
    temp[3] = num//8
    num = num % 8
    temp[2] = num // 4
    num = num % 4
    temp[1] = num // 2
    temp[0] = num % 2
    return temp

castle = []
for _ in range(m):
    temp = list(map(int, input().split()))
    castle.append(temp)

castle_wall = [ [0] * n for _ in range(m) ]
for i in range(m):
    for j in range(n):
        castle_wall[i][j] = make_bitway(castle[i][j])

D = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def find_room(i, j):
    global cnt
    cnt += 1
    new_castle[i][j] = room_num
    for k in range(4):
        if castle_wall[i][j][k] == 0:
            idy = i + D[k][0]
            jdx = j + D[k][1]
            if 0 <= idy < m and 0 <= jdx < n:
                if k == 0:
                    if castle_wall[idy][jdx][2] == 0 and new_castle[idy][jdx] == 0:
                        find_room(idy, jdx)
                if k == 1:
                    if castle_wall[idy][jdx][3] == 0 and new_castle[idy][jdx] == 0:
                        find_room(idy, jdx)
                if k == 2:
                    if castle_wall[idy][jdx][0] == 0 and new_castle[idy][jdx] == 0:
                        find_room(idy, jdx)
                if k == 3:
                    if castle_wall[idy][jdx][1] == 0 and new_castle[idy][jdx] == 0:
                        find_room(idy, jdx)

new_castle = [ [0] * n for _ in range(m) ]
castle_dict = {}
room_num = 1
for i in range(m):
    for j in range(n):
        cnt = 0
        if new_castle[i][j] == 0:
            find_room(i, j)
            castle_dict[room_num] = cnt
            room_num += 1

result1 = max(castle_dict.keys())
result2 = max(castle_dict.values())

def find_max_room(i, j):
    global max_room
    key = new_castle[i][j]
    value = castle_dict[key]
    for k in range(4):
        idy = i + D[k][0]
        jdx = j + D[k][1]
        if 0 <= idy < m and 0 <= jdx < n:
            if new_castle[idy][jdx] != key:
                value2 = castle_dict[new_castle[idy][jdx]]
                if value + value2 > max_room:
                    max_room = value + value2

max_room = 0
for i in range(m):
    for j in range(n):
        find_max_room(i, j)

result3 = max_room
print(result1)
print(result2)
print(result3)