import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    tc_num = int(input())
    total_list = []
    max_sum = 0
    diag1 = 0
    diag2 = 0

    for k in range(100):
        temp_list = list(map(int, input().split()))
        total_list.append(temp_list)
        sum_temp_list = sum(temp_list)
        if max_sum < sum_temp_list:
            max_sum = sum_temp_list
    
    for j in range(100):
        hang_sum = 0
        for i in range(100):
            hang_sum += total_list[i][j]
        if max_sum < hang_sum:
            max_sum = hang_sum

    for l in range(100):
        diag1 += total_list[l][l]
    if max_sum < diag1:
        max_sum = diag1
    
    for h in range(100):
        diag2 += total_list[h][99-h]
    if max_sum < diag2:
        max_sum = diag2
    
    print("#%d %d" %(tc,max_sum))