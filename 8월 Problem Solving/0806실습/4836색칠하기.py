T = int(input())

for tc in range(1, T + 1):
    base_list = []
    for i in range(10):
        base_list.append([0]*10)
    cnt = 0

    N = int(input())
    for N_num in range(1, N+1):
        color_index = list(map(int, input().split()))
        # LT 는 Left Top, RB는 Right Bottom, x는 x좌표, y는 y좌표, CN은 color number
        LTx = color_index[0]
        LTy = color_index[1]
        RTx = color_index[2]
        RTy = color_index[3]
        CN = color_index[4]
        for x in range(LTx, RTx + 1):
            for y in range(LTy, RTy + 1):
                base_list[x][y] += CN

    for i in range(10):
        for j in range(10):
            if base_list[i][j] >= 3:
                cnt += 1

    print("#%d %d" %(tc, cnt))