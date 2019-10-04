import sys
sys.stdin = open("2115_input.txt", "r")
import itertools

def honeybutterchip(list):
    extract_max = 0
    cnt = 1
    # 여기 일단 itertools 쓰고 이따가 다시 복습해보자.
    while cnt < M + 1:
        butter = itertools.combinations(list, cnt)
        for chip in butter:
            if sum(chip) > C:
                continue
            else:
                temp = 0
                for hon in chip:
                    temp += (hon ** 2)
                if temp > extract_max:
                    extract_max = temp
        cnt += 1
    return extract_max

T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    honey = list()
    for _ in range(N):
        honey.append(list(map(int, input().split())))
    NM = N - M + 1
    max_honey = 0

    for i in range(N):
        for j in range(NM):
            pooh = []
            for k in range(M):
                pooh.append(honey[i][j + k])
            honey_obtained1 = honeybutterchip(pooh)
            # print("1",pooh)
            if j + M  < NM:
                for m in range(j + M, NM):
                    pooh2 = []
                    for n in range(M):
                        pooh2.append(honey[i][j + M + n])
                    honey_obtained2 = honeybutterchip(pooh2)
                    if honey_obtained1 + honey_obtained2 > max_honey:
                        max_honey = honey_obtained1 + honey_obtained2
            for a in range(i + 1, N):
                for b in range(NM):
                    pooh3 = []
                    for c in range(M):
                        pooh3.append(honey[a][b + c])
                    honey_obtained2 = honeybutterchip(pooh3)
                    if honey_obtained1 + honey_obtained2 > max_honey:
                        max_honey = honey_obtained1 + honey_obtained2
    
    print("#%d %d" %(tc, max_honey))