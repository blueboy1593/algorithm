import sys
sys.stdin = open("2805_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [0] * N
    for k in range(N):
        farm[k] = list(map(int, input()))

    ban = (N-1) // 2
    value = 0

    for i in range(ban):
        value += farm[i][ban]
        value += farm[N - 1 - i][ban]
        for j in range(1, i + 1):
            value += farm[i][ban + j]
            value += farm[i][ban - j]
            value += farm[N-1-i][ban + j]
            value += farm[N - 1 - i][ban - j]
    for a in farm[ban]:
        value += a

    print("#%d %d" %(tc, value))