from pprint import pprint

N = int(input())
mymap = []
mydict = {}
danjisoo = []
for i in range(N):
    temp = list(map(int, input()))
    mymap.append(temp)
# 지도 생성 및 인풋값 받기

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def jaegui(y, x, dangi):
    global N
    mymap[y][x] = dangi
    for j in range(4):
        ddy = y + dy[j]
        ddx = x + dx[j]
        if 0 <= ddy < N and 0 <= ddx < N and mymap[ddy][ddx] == 1:
            jaegui(ddy, ddx, dangi)

dangi = 2
for i in range(N):
    for j in range(N):
        if mymap[i][j] == 1:
            jaegui(i, j, dangi)
            mydict[dangi] = 0
            dangi += 1

for i in range(N):
    for j in range(N):
        if mymap[i][j] != 0:
            mydict[mymap[i][j]] += 1

total_danjisoo = len(mydict)
for value in mydict.values():
    danjisoo.append(value)
result = sorted(danjisoo)

print(total_danjisoo)
for num in result:
    print(num)