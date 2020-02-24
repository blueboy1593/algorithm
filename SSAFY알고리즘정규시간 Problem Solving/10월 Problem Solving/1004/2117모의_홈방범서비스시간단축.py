import sys
sys.stdin = open("2117_input.txt", "r")

def operation_expense():
    for K in range(22):
        operation_expense_list[K] = K * K + (K - 1) * (K - 1)
    return

def how_much(i, j, K):
    global house_max
    cost = operation_expense_list[K]
    earn = 0
    cnt = 0
    for m in range(N):
        for n in range(N):
            if abs(m - i) + abs(n - j) < K and SECOM[m][n] == 1:
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
    operation_expense_list = [0] * 22
    operation_expense()

    for i in range(N):
        for j in range(N):
            for K in range(1, N + 2):
                how_much(i, j, K)
    
        
    print("#%d %d" %(tc, house_max))