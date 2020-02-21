N, M, H = map(int, input().split())

ladder = [ [0] * (N + 2) for _ in range(H + 2) ]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = 1
    ladder[a][b + 1] = 2
# print(*ladder, sep="\n")
# 여기까지가 기존 사다리 표현법!
# 아예 늘려버렸다. 이게 계산하기 더 쉬울 수도 있어.

def sadaritagi(j):
    initial_j = j
    i = 1
    while i < H + 1:
        if ladder[i][j] == 1:
            j += 1
        elif ladder[i][j] == 2:
            j -= 1
        i += 1
    if initial_j == j:
        return True
    else:
        return False

# 2번 Logic. 좌표 조합 찾기. 1, 2, 3, 다!
result = -1
flag = True
for k in range(1, N + 1):
    rr = sadaritagi(k)
    if rr == False:
        flag = False
        break
if flag == True:
    result = 0

# 1개짜리 사다리 좌표로 정리해보기.
if result == -1:
    for i in range(1, H + 1):
        for j in range(1, N):
            # print(i, j)
            if ladder[i][j] == 0 and ladder[i][j + 1] == 0: # 맵을 넓힘으로서 한번에 위치할 수 있게 하기.
                ladder[i][j] = 1
                ladder[i][j + 1] = 2
                # print(*ladder, sep='\n')
                # print('------------------------------------------------------')
                flag = True
                for k in range(1, N + 1):
                    rr = sadaritagi(k)
                    # print(rr)
                    if rr == False:
                        flag = False
                if flag == True:
                    result = 1
                # 여기서 2번 들어가보자.
                for jj in range(j + 1, N):
                    if ladder[i][jj] == 0 and ladder[i][jj + 1] == 0:
                        ladder[i][jj] = 1
                        ladder[i][jj + 1] = 2
                        # print(*ladder, sep='\n')
                        # print('------------------------------------------------------')
                        flag = True
                        for k in range(1, N + 1):
                            rr = sadaritagi(k)
                            # print(rr)
                            if rr == False:
                                flag = False
                        if flag == True:
                            if result == -1 or result == 3:
                                result = 2

                        for jjj in range(jj + 1, N):
                            if ladder[i][jjj] == 0 and ladder[i][jjj + 1] == 0:
                                ladder[i][jjj] = 1
                                ladder[i][jjj + 1] = 2
                                # print(*ladder, sep='\n')
                                # print('------------------------------------------------------')
                                flag = True
                                for k in range(1, N + 1):
                                    rr = sadaritagi(k)
                                    # print(rr)
                                    if rr == False:
                                        flag = False
                                if flag == True:
                                    if result == -1:
                                        result = 3
                                ladder[i][jjj] = 0
                                ladder[i][jjj + 1] = 0

                        for iii in range(i + 1, H + 1):
                            for jjj in range(1, N):
                                if ladder[iii][jjj] == 0 and ladder[iii][jjj + 1] == 0:
                                    ladder[iii][jjj] = 1
                                    ladder[iii][jjj + 1] = 2
                                    # print(*ladder, sep='\n')
                                    # print('------------------------------------------------------')
                                    flag = True
                                    for k in range(1, N + 1):
                                        rr = sadaritagi(k)
                                        # print(rr)
                                        if rr == False:
                                            flag = False
                                    if flag == True:
                                        if result == -1:
                                            result = 3
                                    ladder[iii][jjj] = 0
                                    ladder[iii][jjj + 1] = 0
                        ladder[i][jj] = 0
                        ladder[i][jj + 1] = 0

                for ii in range(i + 1, H + 1):
                    for jj in range(1, N):
                        if ladder[ii][jj] == 0 and ladder[ii][jj + 1] == 0:
                            ladder[ii][jj] = 1
                            ladder[ii][jj + 1] = 2
                            # print(*ladder, sep='\n')
                            # print('------------------------------------------------------')
                            flag = True
                            for k in range(1, N + 1):
                                rr = sadaritagi(k)
                                # print(rr)
                                if rr == False:
                                    flag = False
                            if flag == True:
                                if result == -1 or result == 3:
                                    result = 2

                            for jjj in range(jj + 1, N):
                                if ladder[ii][jjj] == 0 and ladder[ii][jjj + 1] == 0:
                                    ladder[ii][jjj] = 1
                                    ladder[ii][jjj + 1] = 2
                                    # print(*ladder, sep='\n')
                                    # print('------------------------------------------------------')
                                    flag = True
                                    for k in range(1, N + 1):
                                        rr = sadaritagi(k)
                                        # print(rr)
                                        if rr == False:
                                            flag = False
                                    if flag == True:
                                        if result == -1:
                                            result = 3
                                    ladder[ii][jjj] = 0
                                    ladder[ii][jjj + 1] = 0

                            for iii in range(ii + 1, H + 1):
                                for jjj in range(1, N):
                                    if ladder[iii][jjj] == 0 and ladder[iii][jjj + 1] == 0:
                                        ladder[iii][jjj] = 1
                                        ladder[iii][jjj + 1] = 2
                                        # print(*ladder, sep='\n')
                                        # print('------------------------------------------------------')
                                        flag = True
                                        for k in range(1, N + 1):
                                            rr = sadaritagi(k)
                                            # print(rr)
                                            if rr == False:
                                                flag = False
                                        if flag == True:
                                            if result == -1:
                                                result = 3
                                        ladder[iii][jjj] = 0
                                        ladder[iii][jjj + 1] = 0
                            ladder[ii][jj] = 0
                            ladder[ii][jj + 1] = 0
                ladder[i][j] = 0
                ladder[i][j + 1] = 0

print(result)