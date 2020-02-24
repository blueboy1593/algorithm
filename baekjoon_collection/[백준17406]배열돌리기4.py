from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
C_baeyeol = []
for _ in range(N):
    C_baeyeol.append(list(map(int, input().split())))

K_list = []
for k in range(K):
    r, c, s = map(int, input().split())
    r -= 1
    c -= 1
    K_list.append((r, c, s))
minmin = 9999999999

# permu까지 구하자.
K_permu = list(permutations(range(K)))
for perm in K_permu:
    baeyeol = deepcopy(C_baeyeol)
    # 각각의 순열
    for p in perm:
        r, c, s = K_list[p]
        # print(r, c, s)
        for ss in range(1, s + 1):
            i = r - ss
            j = c - ss
            saved_value = baeyeol[i][j]
            for _ in range(2*ss): # 아래루다가
                ii = i
                i = i + 1
                baeyeol[ii][j] = baeyeol[i][j]
            for _ in range(2*ss): # 오른쪽
                jj = j
                j += 1
                baeyeol[i][jj] = baeyeol[i][j]
            for _ in range(2*ss): # 위
                ii = i
                i = i - 1
                baeyeol[ii][j] = baeyeol[i][j]
            for _ in range(2*ss - 1): # 왼쪽
                jj = j
                j -= 1
                baeyeol[i][jj] = baeyeol[i][j]
            baeyeol[i][j] = saved_value
        # print(*baeyeol, sep='\n')
        # print('----------------------절취선----------------------')
    
    for h in range(N):
        temp = sum(baeyeol[h])
        if temp < minmin:
            minmin = temp

print(minmin)