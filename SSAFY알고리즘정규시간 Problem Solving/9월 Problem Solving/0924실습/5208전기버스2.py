import sys
sys.stdin = open("5208_input.txt", "r")

def backtrack(i, cnt):
    global min_cnt
    dis_possible = lpg_list[i]
    if i + dis_possible >= N:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    else:
        cnt += 1
        if cnt > min_cnt:
            return
        for j in range(1, dis_possible + 1):
            i = i + j
            if i < N:
                backtrack(i, cnt)
            i = i - j

T = int(input())

for tc in range(1, T + 1):
    lpg_list = list(map(int, input().split()))
    N = lpg_list[0]
    min_cnt = 999
    cnt = 1

    gas = lpg_list[1]
    for k in range(1, gas + 1):
        backtrack(1 + k, cnt)

    print("#%d %d" %(tc,min_cnt))