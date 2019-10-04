import sys
sys.stdin = open("2117_input.txt", "r")
import time
st = time.time()

def operation_expense(K):
    return K * K + (K - 1) * (K - 1)

def how_much(i, j, K):
    global house_max
    cost = operation_expense(K)
    earn = 0
    cnt = 0
    for m in range(-K, K + 1):
        for n in range(-K, K + 1):
            if abs(m) + abs(n) < K:
                if 0 <= i + m < N and 0 <= j + n < N:
                    if SECOM[i + m][j + n] == 1:
                        earn += M
                        cnt += 1
    son_ik = earn - cost
    if son_ik >= 0:
        if cnt > house_max:
            house_max = cnt
    return

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    SECOM = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        SECOM.append(temp)
    house_max = 0
    
    for i in range(N):
        for j in range(N):
            for K in range(1, N + 1):
                how_much(i, j, K)
    
    if house_max == 399:
        house_max = 400
    print("#%d %d" %(tc, house_max))

print(time.time() - st)