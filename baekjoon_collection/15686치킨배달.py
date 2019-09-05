import itertools
result = 99999

def distance(chicken):
    global result, cnt, N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if chicken[i][j] == 1:
                find_short(i, j, chicken)
    print(cnt)
    if cnt < result:
        result = cnt

def find_short(i, j, chicken):
    global cnt, N
    visited = [[False] * N for _ in range(N)]
    queue = [[i, j]]
    dis = 1
    while queue:
        for _ in range(len(queue)):
            a = queue.pop(0)
            for k in range(4):
                idy = a[0] + dy[k]
                idx = a[1] + dx[k]
                if 0 <= idy < N and 0 <= idx < N:
                    if chicken[idy][idx] == 2:
                        cnt += dis
                        return
                    if visited[idy][idx] == False:
                        visited[idy][idx] = True
                        queue.append([idy, idx])
        dis += 1

N, M = map(int, input().split())
original_chicken = []
for _ in range(N):
    temp = list(map(int, input().split()))
    original_chicken.append(temp)
chicken_list = []
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for i in range(N):
    for j in range(N):
        if original_chicken[i][j] == 2:
            chicken_list.append([i, j])
            original_chicken[i][j] = 0

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

    distance(chicken)

print(result)
