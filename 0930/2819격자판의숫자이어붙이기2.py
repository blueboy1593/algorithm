import sys
sys.stdin = open("2819_input.txt", "r")

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(i, j, cnt, number):
    number += str(grid[i][j])
    cnt += 1
    if cnt == 7:
        if number not in num_list:
            num_list.append(number)
        return
    else:
        for k in range(4):
            idy = i + dy[k]
            idx = j + dx[k]
            if 0 <= idy < 4 and 0 <= idx < 4:
                DFS(idy, idx, cnt, number)


for tc in range(1, T + 1):
    grid = [0] * 4
    for i in range(4):
        grid[i] = list(map(int, input().split()))
    num_list = []
    TF = [ [False] * 4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            cnt = 0
            number = ''
            DFS(i, j , cnt, number)
            

    print("#%d %d" %(tc, len(num_list)))