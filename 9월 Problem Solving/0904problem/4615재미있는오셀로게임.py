import sys
sys.stdin = open("4615_input.txt", "r")

T = int(input())
dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]
def gogo(y, x):
    global by, bx, dol, suk
    temp_dol.append([y,x])
    if y + by < 0 or y + by > N -1 or x + bx < 0 or x + bx > N - 1:
        return
    if oselo_map[y + by][x + bx] == dol:
        for temp in temp_dol:
            oselo_map[temp[0]][temp[1]] = dol
        return
    if oselo_map[y + by][x + bx] == 0:
        return
    if oselo_map[y + by][x + bx] == suk:
        gogo(y + by, x + bx)


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    oselo = []
    for _ in range(M):
        temp = list(map(int, input().split()))
        oselo.append(temp)
    oselo_map = [ [0] * N for _ in range(N) ]
    half = N//2
    oselo_map[half][half] = 2
    oselo_map[half-1][half-1] = 2
    oselo_map[half - 1][half] = 1
    oselo_map[half][half - 1] = 1

    for info in oselo:
        y = info[1] - 1
        x = info[0] - 1
        dol = info[2]
        if dol == 2:
            suk = 1
        if dol == 1:
            suk = 2
        oselo_map[y][x] = dol
        for j in range(8):
            by = dy[j]
            bx = dx[j]
            cy = y + dy[j]
            cx = x + dx[j]
            try:
                if oselo_map[cy][cx] == suk:
                    temp_dol = []
                    gogo(cy, cx)
            except:
                pass

    black = 0
    white = 0

    for i in range(N):
        for j in range(N):
            if oselo_map[i][j] == 1:
                black += 1
            if oselo_map[i][j] == 2:
                white += 1

    print("#%d %d %d" %(tc, black, white))