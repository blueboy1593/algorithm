import sys
sys.stdin = open("2382_input.txt", "r")

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

def micromove(organism):
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a = organism[i][j]
            if a != 0:
                a[0] = a[0] + dy[a[3]]
                a[1] = a[1] + dx[a[3]]
                y = a[0]
                x = a[1]
                b = arr[y][x]
                if b == 0:
                    if y == 0 or y == N - 1 or x == 0 or x == N - 1:
                        a = micro_reduce(a)
                        arr[y][x] = a
                    else:
                        arr[y][x] = a
                elif len(b) == 4:
                    arr[y][x] = [b, a]
                    stack.append([y, x])
                else:
                    arr[y][x].append(a)
    return arr

def micro_reduce(mic):
    mic[2] = mic[2] // 2
    if mic[3] == 1 or mic[3] == 3:
        mic[3] += 1
    else:
        mic[3] -= 1
    return mic

def micro_battle(s):
    y = s[0]
    x = s[1]
    battle = bin[y][x]
    battle.sort(reverse=True)
    micro_num = 0
    for i in range(len(battle)):
        micro_num += battle[i][2]
    dab = [y, x, micro_num, battle[0][3]]
    return dab

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    m = 0
    stack = []
    bin = [[0] * N for _ in range(N)]
    result = 0

    micro = []
    for _ in range(K):
        temp = list(map(int, input().split()))
        micro.append(temp)

    for orga in micro:
        y = orga[0]
        x = orga[1]
        bin[y][x] = orga

    while m != M:
        m += 1
        bin = micromove(bin)

        while stack:
            s = stack.pop()
            ss = micro_battle(s)
            bin[ss[0]][ss[1]] = ss

    for i in range(N):
        for j in range(N):
            if bin[i][j] != 0:
                result += bin[i][j][2]

    print("#%d %d" %(tc, result))