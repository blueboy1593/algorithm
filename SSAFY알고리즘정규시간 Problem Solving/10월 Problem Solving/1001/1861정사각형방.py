import sys
sys.stdin = open("1861_input.txt", "r")

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def isWall(y, x):
    if 0 <= y < N and 0 <= x < N:
        return True

def fake_BFS(i, j, num):
    # num_save = num
    cnt = 1
    while True:
        flag = 0
        check_list[num] = True
        for k in range(4):
            idy = i + dy[k]
            jdx = j + dx[k]
            # print(i, j, idy, jdx)
            if isWall(idy, jdx):
                if room[idy][jdx] == num + 1:
                    
                    num += 1
                    flag = 1
                    cnt += 1
                    # print(idy, jdx, num, cnt)
                    break
                # if room[idy][jdx] == num - 1:
                #     return
        if flag == 0:
            return cnt
        
        i = idy
        j = jdx

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [0] * N
    for i in range(N):
        room[i] = list(map(int, input().split()))
    bang = 0
    final_num = 0
    check_list = [False] * (N*N + 1)

    for i in range(N):
        for j in range(N):
            num = room[i][j]
            if check_list[num] == False:
                cnt = fake_BFS(i, j, num)
                if cnt != None:
                    if bang < cnt:
                        bang = cnt
                        final_num = num
                    elif bang == cnt:
                        if final_num > num:
                            final_num = num

    print("#%d %d %d" %(tc, final_num, bang))