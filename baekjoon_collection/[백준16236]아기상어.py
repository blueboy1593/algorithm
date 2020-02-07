N = int(input())
shark_map = []
for _ in range(N):
    shark_map.append(list(map(int, input().split())))
size = 2
size_stack = 0
D = [(0,1), (0,-1), (1,0), (-1,0)]
# 기본 맵 설정
answer_time = 0

# 1단계 아기상어 시작 위치 잡기.
for i in range(N):
    for j in range(N):
        # 아기상어 시작 위치
        if shark_map[i][j] == 9:
            start = (i, j)
            shark_map[i][j] = 0

# 이 문제에서 가장 중요한 logic이 담겨있는 함수!
def bfs(y, x):
    global size
    time = 0
    visited = [ [False] * N for _ in range(N) ]
    queue = [(y, x)]
    visited[y][x] = True
    while queue:
        time += 1
        for _ in range(len(queue)):
            que = queue.pop(0)
            y, x = que
            for k in range(4):
                idy = y + D[k][0]
                jdx = x + D[k][1]
                # iswall
                if 0 <= idy < N and 0 <= jdx < N:
                    # BFS 할때 전형적으로 쓰는거.
                    if visited[idy][jdx] == False:
                        visited[idy][jdx] = True
                        # size가 더 큰 곳은 1로 표현되어있고 못감!
                        if temp_shark_map[idy][jdx] == 0:
                            queue.append((idy, jdx))
                            # 물고기 로직 들어가야함!!
                            # 0보다는 커야지...
                            if 0 < shark_map[idy][jdx] < size:
                                # 나중에 lahmda로 정렬하자! 연습해야함.
                                will_eat.append([idy, jdx])
        if will_eat != []:
            # print('시간', time)
            # print(will_eat)
            return time
    return False

# 엄마에게 요청 보낼 때까지
while True:
    # 1번 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    # 이거 길...까지 고려해야하는데 한번에 처리했어야...ㅎ
    flag = False
    for i in range(N):
        for j in range(N):
            # 먹을게 있다면?
            if 0 < shark_map[i][j] < size:
                flag = True
                break
        if flag == True:
            break
    # 먹을게 없으면 탈출
    if flag == False:
        break

    # 1.5번 벽 세워버리기! 신맵 재설정 과정
    temp_shark_map = [ [0] * N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            if shark_map[i][j] > size:
                temp_shark_map[i][j] = 1

    # list와 bfs로 먹을 수 있는 물고기 모두 탐색!!
    will_eat = []
    # 길이 막혀있는지를 같이 점검을 해야하는구나...ㅠㅠ
    time_costed = bfs(start[0], start[1])
    if type(time_costed) == int:
        answer_time += time_costed
    else:
        break

    # 2번 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    if len(will_eat) == 1:
        y, x = will_eat[0]
        shark_map[y][x] = 0
        # 잡아먹고 위치 바꾸기
        start = (y, x)
    # 3번 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    else:
        will_eat.sort() # 이거 낮은거부터 정렬 맞나...?
        y, x = will_eat[0]
        shark_map[y][x] = 0
        # 잡아먹고 위치 바꾸기
        start = (y, x)

    size_stack += 1
    if size_stack == size:
        size += 1
        size_stack = 0

print(answer_time)

# 아오씨 조건...
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.