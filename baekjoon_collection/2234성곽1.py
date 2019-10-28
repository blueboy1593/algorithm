from pprint import pprint

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

def find_room(i, j, cnt):
    global cnt
    cnt += 1
    new_castle[i][j] = room_num
    for k in range(4):
        if castle_wall[i][j][k] == 0:
            idy = i + D[k][0]
            jdx = j + D[k][1]
            if 0 <= idy < m and 0 <= jdx < n:
                if 


new_castle = [ [0] * n for _ in range(m) ]
for i in range(m):
    for j in range(n):
        cnt = 0
        room_num = 1
        find_room(i, j, cnt)

pprint(castle_wall)
