import sys
sys.stdin = open("5105_input.txt", "r")

dx = [0,0,1,-1]
dy = [1,-1,0,0]

T = int(input())

for t in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # pprint(maze)

    def FindInx():
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    return [i,j]
    cnt = 0
    queue = [FindInx()]
    flag = 0
    while queue:

        if flag == 1:
            break
        cnt -= 1
        for i in range(len(queue)):
            temp_x = queue[0][0]
            temp_y = queue[0][1]
            queue.pop(0)
            for j in range(4):
                if 0 <= temp_x + dx[j] < N and 0 <= temp_y + dy[j] < N:
                    if maze[temp_x + dx[j]][temp_y + dy[j]] == 0:
                        maze[temp_x + dx[j]][temp_y + dy[j]] = cnt
                        queue.append([temp_x + dx[j], temp_y + dy[j]])
                    if maze[temp_x + dx[j]][temp_y + dy[j]] == 3:
                        flag = 1
                        break
            if flag == 1:
                break

    #if flag == 0:
    #    cnt = -1
    result = -cnt -1
    if flag == 0:
        result = 0

    print('#' + str(t+1) + ' ', end = '')
    print(result)