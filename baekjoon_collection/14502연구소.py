N, M = map(int, input().split())
virus = [0] * N
d = [(1,0), (-1,0), (0,1), (0,-1)]
maxmax = 0

for i in range(N):
    virus[i] = list(map(int, input().split()))

def baechi_one(a, b, c):
    copy_virus = [i[:] for i in virus]
    copy_virus[a[0]][a[1]] = 1
    copy_virus[b[0]][b[1]] = 1
    copy_virus[c[0]][c[1]] = 1
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if copy_virus[i][j] == 2:
                virus_go(i, j, visited, copy_virus)
    find_safetyzone(copy_virus)

def virus_go(y, x, visited, copy_virus):
    visited[y][x] = True
    copy_virus[y][x] = 2
    for dy, dx in d:
        cdy = y + dy
        cdx = x + dx
        if 0 <= cdy < N and 0 <= cdx < M:
        # try:
            if visited[cdy][cdx] == False and copy_virus[cdy][cdx] == 0:
                virus_go(cdy, cdx, visited, copy_virus)
        # except IndexError:
            # pass

def find_safetyzone(copy_virus):
    global safety, maxmax
    safety = 0
    for i in range(N):
        for j in range(M):
            if copy_virus[i][j] == 0:
                safety += 1
    if safety > maxmax:
        maxmax = safety

zero_list = []
for i in range(N):
    for j in range(M):
        if virus[i][j] == 0:
            zero_list.append([i,j])

len_zero = len(zero_list)
for i in range(len_zero):
    for j in range(i+1, len_zero):
        for k in range(j+1, len_zero):
            a = zero_list[i]
            b = zero_list[j]
            c = zero_list[k]
            baechi_one(a, b, c)

print(maxmax)