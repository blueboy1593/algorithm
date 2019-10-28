from pprint import pprint
import copy

N, M, H = map(int, input().split())

ladder = [ [0] * (N + 1) for _ in range(H + 1) ]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = 1
    ladder[a][b + 1] = 2

def sadaritagi(i, j, ladderr):
    initial_j = j
    while i < H:
        i += 1
        if ladderr[i][j] == 1:
            j += 1
        elif ladderr[i][j] == 2:
            j -= 1
    
    if initial_j == j:
        return True
    else:
        return False

pprint(ladder)

result = -1
flag = False
stop = False
for k in range(1, N + 1):
    if sadaritagi(0, k, ladder) == False:
        stop = True
        break
if stop == False:
    result = 0

else:
    for i in range(1, H + 1):
        for j in range(1, N):
            if ladder[i][j] == 0 and ladder[i][j + 1] == 0:
                ladder[i][j] = 1
                ladder[i][j + 1] = 2
                # pprint(ladder)
                stop = False
                for k in range(1, N + 1):
                    if sadaritagi(0, k, ladder) == False:
                        stop = True
                        break

                if stop == False:
                    result = 1
                    flag = True
                
                if flag == True:
                    break
                
                ladder2 = copy.deepcopy(ladder)
                pprint(ladder)
                pprint(ladder2)
                for i in range(1, H + 1):
                    for j in range(1, N):
                        if ladder2[i][j] == 0 and ladder2[i][j + 1] == 0:
                            ladder2[i][j] = 1
                            ladder2[i][j + 1] = 2
                            stop = False
                            for k in range(1, N + 1):
                                if sadaritagi(0, k, ladder2) == False:
                                    stop = True
                                    break

                            if stop == False:
                                result = 2
                                flag = True
                            
                            if flag == True:
                                break
                            # pprint(ladder2)

                            # ladder3 = copy.deepcopy(ladder2)
                            # for i in range(1, H + 1):
                            #     for j in range(1, N):
                            #         if ladder3[i][j] == 0 and ladder3[i][j + 1] == 0:
                            #             ladder3[i][j] = 1
                            #             ladder3[i][j + 1] = 2
                            #             stop = False
                            #             for k in range(1, N + 1):
                            #                 if sadaritagi(0, k, ladder3) == False:
                            #                     stop = True
                            #                     break

                            #             if stop == False:
                            #                 result = 3
                            #                 flag = True
                                        
                            #             ladder3[i][j] = 0
                            #             ladder3[i][j + 1] = 0
                            #         if flag == True:
                            #             break
                            #     if flag == True:
                            #         break

                            ladder2[i][j] = 0
                            ladder2[i][j + 1] = 0
                        if flag == True:
                            break
                    if flag == True:
                        break

                ladder[i][j] = 0
                ladder[i][j + 1] = 0
            if flag == True:
                break
        if flag == True:
            break

print(result)
