dice = list(map(int, input().split()))
# 시작부터 도착까지
long_line = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0]
line10 = [0, 13, 16, 19]
line20 = [0, 22, 24]
line30 = [0, 28, 27, 26]
line25 = [0, 25, 30, 35, 40]
# 40에 대해서는 어떻게 해야할지 좀 어렵네.
total_map= [long_line, line10, line20, line30, line25]
print(total_map)

def dice_backtracking(cnt, score):
    if cnt == 9:
        print(score)
        return
    cnt += 1
    dice_num = dice[cnt]
    for i in range(4):
        pre_position_line = dice_index[i][0]
        pre_position_index = dice_index[i][1]


dice_index = [0] * 4
score = long_line[dice[0]]
dice_index[0] = [0, dice[0]]
dice_backtracking(0, score)

