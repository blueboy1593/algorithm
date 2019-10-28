import sys
sys.stdin = open("5247_input.txt", "r")
import time
start = time.time()

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    yonsan = [0] * (1000001)
    visited = [0] * (1000001)
    yonsan[N] = 1

    def do_yonsan(i, cnt):
        cnt += 1
        new_1 = i + 1
        new_2 = i - 1
        new_3 = i * 2
        new_4 = i - 10
        if new_1 < M + 1:
            if yonsan[new_1] == 0:
                yonsan[new_1] = cnt
            else:
                if cnt < yonsan[new_1]:
                    yonsan[new_1] = cnt
                    visited[new_1] = False
        if new_2 > 0:
            if yonsan[new_2] == 0:
                yonsan[new_2] = cnt
            else:
                if cnt < yonsan[new_2]:
                    yonsan[new_2] = cnt
                    visited[new_2] = False
        if new_3 < M * 2 + 1 and new_3 <= 1000000:
            if yonsan[new_3] == 0:
                yonsan[new_3] = cnt
            else:
                if cnt < yonsan[new_3]:
                    yonsan[new_3] = cnt
                    visited[new_3] = False
        if new_4 > 0:
            if yonsan[new_4] == 0:
                yonsan[new_4] = cnt
            else:
                if cnt < yonsan[new_4]:
                    yonsan[new_4] = cnt
                    visited[new_4] = False
    cutcut = 99999999
    flag = False
    while True:
        flag = False
        for i in range(1000001):
            if yonsan[i] != 0 and visited[i] == False and yonsan[i] < cutcut:
                do_yonsan(i, yonsan[i])
                visited[i] = True
                flag = True
        if yonsan[M] != 0:
            cutcut = yonsan[M]
        if flag == False:
            break

    print("#%d %d" %(tc, yonsan[M] - 1))
print(time.time() - start)