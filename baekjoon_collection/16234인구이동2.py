N, L, R = map(int, input().split())
population = [ list(map(int, input().split())) for _ in range(N) ]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
flag = 1
cnt = -1

def find_union(i, j):
    global flag
    queue = [[i, j]]
    union = []
    while queue:
        for _ in range(len(queue)):
            a = queue.pop(0)
            y = a[0]
            x = a[1]
            b = population[y][x]
            for k in range(4):
                idy = y + dy[k]
                idx = x + dx[k]
                if 0 <= idy < N and 0 <= idx < N:
                    if visited[idy][idx] == False:
                        c = population[idy][idx]
                        if L <= abs(b - c) <= R:
                            visited[idy][idx] = True
                            if union == []:
                                union.append([y, x, b])
                            union.append([idy, idx, c])
                            queue.append([idy, idx])
                            flag = 1
    if union:
        union_list.append(union)

def sum_union(uni):
    total = 0
    total_num = 0
    for un in uni:
        total += un[2]
        total_num += 1
    average = total//total_num
    for un in uni:
        a = un[0]
        b = un[1]
        population[a][b] = average


while flag == 1:
    flag = 0
    cnt += 1
    visited = [ [False] * N for _ in range(N) ]
    union_list = []
    for i in range(N):
        for j in range(N):
            if (i + j) % 2 == 0:
                if visited[i][j] == False:
                    visited[i][j] = True
                    find_union(i, j)
    for uni in union_list:
        sum_union(uni)

print(cnt)