import sys
sys.stdin = open("2001_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pari = []
    max_pari = 0
    for _ in range(N):
        pari += [list(map(int, input().split()))]

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp_pari = 0
            for m in range(M):
                for n in range(M):
                    temp_pari += pari[i+m][j+n]
            if temp_pari > max_pari:
                max_pari = temp_pari
    print("#%d %s" %(tc, max_pari))