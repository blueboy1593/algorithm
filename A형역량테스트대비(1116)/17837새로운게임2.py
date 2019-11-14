N, K = map(int, input().split())
# 처음 해보는 연장된 체스판 만들어보기
chess_pan = []
for _ in range(N):
    temp = list(map(int, input().split()))
    chess_pan.append([2] + temp + [2])
chess_pan = [([2] * (N + 2))] + chess_pan + [([2] * (N + 2))]
print(*chess_pan, sep='\n')
# 체스 정보 저장
chess_position_info = [0] * (K + 1)
for i in range(1, K + 1):
    chess_position_info[i] = list(map(int, input().split()))
print(chess_position_info)
cnt = 0
D = [0, (0,1), (0,-1),(-1,0),(1,0)]

chess_ground = [ [0] * (N + 2) for _ in range(N + 2) ]
for i in range(1, K + 1):
    chess = chess_position_info[i]
    y = chess[0]
    x = chess[1]
    direction = chess[2]
    # 방향 정보는 저장 안해도 되겠는데?
    chess_ground[y][x] = [i]
print(*chess_ground, sep='\n')

def change_d(d):
    if d == 4:
        return 3
    elif d == 3:
        return 4
    elif d == 2:
        return 1
    elif d == 1:
        return 2

flag = False
# 본격적인 이동 시작.
while cnt < 10:
    cnt += 1
    for i in range(1, K + 1):
        chess = chess_position_info[i]
        y = chess[0]
        x = chess[1]
        d = chess[2]
        # 슬라이싱 이런거... ㅠㅠ
        if len(chess_ground[y][x]) == 1:
            existed = chess_ground[y][x][:]
            remained = 0
        else:
            for j in range(len(chess_ground[y][x])):
                if chess_ground[y][x][j] == i:
                    existed = chess_ground[y][x][:(j+1)]
                    remained = chess_ground[y][x][(j+1):]
                    if remained == [] or remained == None:
                        remained = 0
        moved_y = y + D[d][0]
        moved_x = x + D[d][1]

        chess_ground[y][x] = remained
        # 파란색일때
        if chess_pan[moved_y][moved_x] == 2:
            d = change_d(d)
            moved_y = y + D[d][0]
            moved_x = x + D[d][1]
            # 맞은편도 파란색일때
            if chess_pan[moved_y][moved_x] == 2:
                moved_y = y
                moved_x = x
            # 체스판에 배정. 일반 색과 동일한 로직 적용
            # 빨간색일때
            if chess_pan[moved_y][moved_x] == 1:
                existed.reverse()
                if chess_ground[moved_y][moved_x] == 0:
                    chess_ground[moved_y][moved_x] = existed
                else:
                    chess_ground[moved_y][moved_x] = chess_ground[moved_y][moved_x] + existed
            elif chess_pan[moved_y][moved_x] == 0:
                if chess_ground[moved_y][moved_x] == 0:
                    chess_ground[moved_y][moved_x] = existed
                else:
                    chess_ground[moved_y][moved_x] = existed + chess_ground[moved_y][moved_x]
            for exist in existed:
                chess_position_info[exist] = [moved_y, moved_x, d]
        # 파란색 마주치지 않았을 때
        else:
            if chess_pan[moved_y][moved_x] == 1:
                existed.reverse()
                if chess_ground[moved_y][moved_x] == 0:
                    chess_ground[moved_y][moved_x] = existed
                # 이미 존재할때
                else:
                    chess_ground[moved_y][moved_x] = chess_ground[moved_y][moved_x] + existed
            elif chess_pan[moved_y][moved_x] == 0:
                if chess_ground[moved_y][moved_x] == 0:
                    chess_ground[moved_y][moved_x] = existed
                # 이미 존재할 때
                else:
                    chess_ground[moved_y][moved_x] = existed + chess_ground[moved_y][moved_x]
            for exist in existed:
                position = chess_position_info[exist][2]
                chess_position_info[exist] = [moved_y, moved_x, position]
        print(*chess_ground, sep='\n')
    #     if len(chess_ground[moved_y][moved_x]) >= 4:
    #         flag = True
    #     if flag == True:
    #         break
    for i in range(N + 2):
        for j in range(N + 2):
            if chess_ground[i][j] != 0:
                if len(chess_ground[i][j]) >= 4:
                    flag = True
    if flag == True:
        break
    print(chess_position_info)

print(cnt)