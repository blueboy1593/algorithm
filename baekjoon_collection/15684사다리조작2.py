from pprint import pprint

N, M, H = map(int, input().split())

ladder = [ [0] * (N + 1) for _ in range(H + 1) ]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = 1
    ladder[a][b + 1] = 2

def sadaritagi(i, j):
    initial_j = j
    while i < H:
        i += 1
        if ladder[i][j] == 1:
            j += 1
        if ladder[i][j] == 2:
            j -= 1
    if initial_j == j:
        return True
    else:
        return False

def make_dari()

result = 0
flag = False
for i in range(1, H + 1):
    for j in range(1, N):
        if ladder[i][j] == 0 and ladder[i][j + 1] == 0:
            ladder[i][j] = 1
            ladder[i][j + 1] = 2
            stop = False
            for k in range(1, N + 1):
                if sadaritagi(0, k) == False:
                    stop = True
                    break
            if stop == False:
                result = 1
                flag = True
            ladder[i][j] = 0
            ladder[i][j + 1] = 0
        if flag == True:
            break
    if flag == True:
        break


pprint(ladder)