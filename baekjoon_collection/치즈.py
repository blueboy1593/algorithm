import sys
sys.stdin = open('input.txt', 'r')

sero, garo = map(int, input().split())
cheeze_map = []
for _ in range(sero):
    temp = list(map(int, input().split()))
    cheeze_map.append(temp)
bin_arr = [[False] * garo for _ in range(sero)]
bin_arr2 = [[False] * garo for _ in range(sero)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0
queue = []

def findhole(y, x):
    global garo, sero
    bin_arr[y][x] = True
    for i in range(4):
        idx = dx[i] + x
        idy = dy[i] + y
        if 0 <= idx < garo and 0 <= idy < sero and cheeze_map[idy][idx] == 0 and bin_arr[idy][idx] == False:
            findhole(idy, idx)

def checkhole():
    for i in range(sero):
        for j in range(garo):
            if cheeze_map[i][j] == 0 and bin_arr[i][j] == False:
                cheeze_map[i][j] = -1

def meltcheeze(y, x):
    global garo, sero
    bin_arr2[y][x] = True
    for i in range(4):
        idx = dx[i] + x
        idy = dy[i] + y
        if 0 <= idx < garo and 0 <= idy < sero and cheeze_map[idy][idx] == 0:
            cheeze_map[y][x] = 2
        if 0 <= idx < garo and 0 <= idy < sero and cheeze_map[idy][idx] == 1 and bin_arr2[idy][idx] == False:
            meltcheeze(idy, idx)

while True:
    cheeze_num = 0
    for i in range(sero):
        for j in range(garo):
            if cheeze_map[i][j] != 1:
                cheeze_map[i][j] = 0
            if cheeze_map[i][j] == 1:
                cheeze_num += 1
    stack.append(cheeze_num)
    if cheeze_map == [ [0]* garo for _ in range(sero) ]:
        break
    findhole(0, 0)
    checkhole()
    for i in range(sero):
        for j in range(garo):
            if cheeze_map[i][j] == 1:
                meltcheeze(i,j)
    bin_arr = [[False] * garo for _ in range(sero)]
    bin_arr2 = [[False] * garo for _ in range(sero)]
    cnt += 1

cheeze = stack[-2]

print(cnt)
print(cheeze)