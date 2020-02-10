from collections import deque

N, M, T = map(int, input().split())
circle_pan = deque()
for _ in range(N):
    temp = deque(list(map(int, input().split())))
    circle_pan.append(temp)
# print(*circle_pan, sep='\n')
xdk = []
for _ in range(T):
    xdk.append(list(map(int, input().split())))

D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def find_injub(i, j, value):
    global flag
    queue = deque([(i, j)])
    inj = [(i, j)]
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            idy = y + D[k][0]
            jdx = x + D[k][1]
            if 0 <= idy < N and 0 <= jdx < M:
                if circle_pan[idy][jdx] == value:
                    if visited[idy][jdx] == False:
                        visited[idy][jdx] = True
                        inj.append((idy, jdx))
                        queue.append((idy, jdx))
        if x == 0 or x == M - 1:
            if x == 0:
                idy, jdx = y, M - 1
            elif x == M - 1:
                idy, jdx = y, 0
            if circle_pan[idy][jdx] == value:
                if visited[idy][jdx] == False:
                    visited[idy][jdx] = True
                    inj.append((idy, jdx))
                    queue.append((idy, jdx))
    if len(inj) > 1:
        for ii in inj:
            circle_pan[ii[0]][ii[1]] = 'x'
            flag = True
        return
    else:
        return

# 1. 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
for xd in xdk:
    x, d, k = xd
    for i in range(N):
        if (i + 1) % x == 0:
            if d == 0:
                for _ in range(k):
                    a = circle_pan[i].pop()
                    circle_pan[i].appendleft(a)
            else:
                for _ in range(k):
                    a = circle_pan[i].popleft()
                    circle_pan[i].append(a)
    # print(*circle_pan, sep='\n')

    flag = False
    visited = [ [ False ] * M for _ in range(N) ]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and circle_pan[i][j] != 'x':
                visited[i][j] = True
                aa = find_injub(i, j, circle_pan[i][j])
    # 인접이 없을 시!
    if flag == False:
        ave = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if circle_pan[i][j] != 'x':
                    ave += circle_pan[i][j]
                    cnt += 1
        # 이거냐 런타임 에러..? 0으로 나누는 경우?
        if cnt != 0:
            average = ave / cnt
            for i in range(N):
                for j in range(M):
                    if circle_pan[i][j] != 'x':
                        if circle_pan[i][j] > average:
                            circle_pan[i][j] -= 1
                        elif circle_pan[i][j] < average:
                            circle_pan[i][j] += 1

    # print(*circle_pan, sep='\n')
result = 0
for i in range(N):
    for j in range(M):
        if circle_pan[i][j] != 'x':
            result += circle_pan[i][j]
print(result)