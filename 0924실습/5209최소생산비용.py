import sys
sys.stdin = open("5209_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    factory = [0] * N
    for i in range(N):
        factory[i] = list(map(int, input().split()))
    min_cnt = 99999

    def do_backtrack(i, line, cnt, TF_list):
        global min_cnt
        if line == N - 1:
            cnt += factory[line][i]
            if cnt < min_cnt:
                min_cnt = cnt
            return
        cnt += factory[line][i]
        if cnt > min_cnt:
            return

        line += 1
        for k in range(N):
            if TF_list[k] == False:
                TF_list[k] = True
                do_backtrack(k, line, cnt, TF_list)
                TF_list[k] = False

    for j in range(N):
        TF_list = [False] * N
        TF_list[j] = True
        cnt = 0
        line = 0
        do_backtrack(j, line, cnt, TF_list)

    print("#%d %d" %(tc,min_cnt))