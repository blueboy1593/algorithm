import sys
sys.stdin = open("1808_input.txt", "r")

T = int(input())

def make_number(num, cnt):
    cnt += 1
    num_save = num
    for su in cal_num:
        num = 10*num_save + su
        if num <= goal:
            if DP_list[num] != 0:
                return
            DP_list[num] = cnt
            number.append([num, cnt])
            make_number(num, cnt)
        else:
            return

for tc in range(1, T + 1):
    calculator = list(map(int, input().split()))
    cal_num = list()
    for i in range(10):
        if calculator[i] == 1:
            cal_num.append(i)
    goal = int(input())
    DP_list = [0] * (goal + 1)
    number = []

    for su in cal_num:
        cnt = 1
        number.append([su, cnt])
        if su <= goal:
            DP_list[su] = 1
            make_number(su, cnt)
    number.sort()

    def jaegui(i):
        for num in number:
                new_num = i * num[0]
                if new_num > goal:
                    return
                else:
                    new_cnt = DP_list[i] + num[1] + 1
                    if DP_list[new_num] != 0:
                        if new_cnt < DP_list[new_num]:
                            DP_list[new_num] = new_cnt
                            jaegui(new_num)
                    else:
                        DP_list[new_num] = new_cnt
                        jaegui(new_num)

    for i in range(len(DP_list)):
        if DP_list[i] != 0:
            jaegui(i)
    result = DP_list[-1] + 1
    if result == 1:
        result = -1

    print("#%d %d" %(tc,result))
                
