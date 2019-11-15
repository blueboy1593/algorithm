import sys
sys.stdin = open("디저트카페_input.txt", "r")

# 리스트 함수 건너가면서 사용하면 안되지만....? 으으으음.
# 함수 내에서 정의한다면?
# 함수 안에서 정의하던 밖에서 정의하던 list는 조심해서 다뤄야한다.
# def wuha(i, j):
#     wuha_cnt = 0
#     temp = [dessert_cafe[i][j]]
#     D = (1, 1)
#     for k in range(1, N):
#         wuha_cnt += 1
#         idy = i + D[0]*k
#         jdx = j + D[1]*k
#         if N <= idy or N <= jdx:
#             return
#         if dessert_cafe[idy][jdx] not in temp:
#             temp.append(dessert_cafe[idy][jdx])
#             zwaha(idy, jdx, temp, wuha_cnt, 0)
#         else:
#             return
#
# def zwaha(i, j, temp, wuha_cnt, zwaha_cnt):
#     # copied_temp = temp[:]
#     D = (1, -1)
#     for k in range(1, N):
#         zwaha_cnt += 1
#         idy = i + D[0] * k
#         jdx = j + D[1] * k
#         if N <= idy or jdx < 0:
#             return
#         if dessert_cafe[idy][jdx] not in temp:
#             temp.append(dessert_cafe[idy][jdx])
#             mamuri(idy, jdx, temp, wuha_cnt, zwaha_cnt)
#         else:
#             return
#
# def mamuri(i, j, temp, wuha_cnt, zwaha_cnt):
#     global dessert
#     # copied_temp = temp[:]
#     D = (-1, -1)
#     for k in range(1, wuha_cnt + 1):
#         idy = i + D[0] * k
#         jdx = j + D[1] * k
#         # 이 조건 안넣었었는데 왜 인덱스 에러가 나지 않지?
#         if N <= idy or jdx < 0 or idy < 0 or N <= jdx:
#             return
#         if dessert_cafe[idy][jdx] not in temp:
#             temp.append(dessert_cafe[idy][jdx])
#         else:
#             return
#     D = (-1, 1)
#     for k in range(1, zwaha_cnt):
#         idy2 = idy + D[0] * k
#         jdx2 = jdx + D[1] * k
#         if dessert_cafe[idy2][jdx2] not in temp:
#             temp.append(dessert_cafe[idy2][jdx2])
#         else:
#             return
#     len_dessert = len(temp)
#     if len_dessert > dessert:
#         dessert = len_dessert
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     dessert_cafe = []
#     for _ in range(N):
#         dessert_cafe.append(list(map(int, input().split())))
#     dessert = -1
#
#     for i in range(N - 2):
#         for j in range(1, N - 1):
#             # 여기서부터 시작
#             # wuha(i, j, [dessert_cafe[i][j]], 0)
#             wuha(i, j)
#
#     print('#%d %d' %(tc, dessert))

def wuha(i, j, temp, wuha_cnt):
    D = (1, 1)
    for k in range(1, N):
        wuha_cnt += 1
        idy = i + D[0]*k
        jdx = j + D[1]*k
        if N <= idy or N <= jdx:
            return
        if dessert_cafe[idy][jdx] not in temp:
            temp.append(dessert_cafe[idy][jdx])
            zwaha(idy, jdx, temp, wuha_cnt, 0)
        else:
            return

def zwaha(i, j, temp, wuha_cnt, zwaha_cnt):
    copied_temp = temp[:]
    D = (1, -1)
    for k in range(1, N):
        zwaha_cnt += 1
        idy = i + D[0] * k
        jdx = j + D[1] * k
        if N <= idy or jdx < 0:
            return
        if dessert_cafe[idy][jdx] not in copied_temp:
            copied_temp.append(dessert_cafe[idy][jdx])
            mamuri(idy, jdx, copied_temp, wuha_cnt, zwaha_cnt)
        else:
            return

def mamuri(i, j, temp, wuha_cnt, zwaha_cnt):
    global dessert
    copied_temp = temp[:]
    D = (-1, -1)
    for k in range(1, wuha_cnt + 1):
        idy = i + D[0] * k
        jdx = j + D[1] * k
        # 이 조건 안넣었었는데 왜 인덱스 에러가 나지 않지?
        if N <= idy or jdx < 0 or idy < 0 or N <= jdx:
            return
        if dessert_cafe[idy][jdx] not in copied_temp:
            copied_temp.append(dessert_cafe[idy][jdx])
        else:
            return
    D = (-1, 1)
    for k in range(1, zwaha_cnt):
        idy2 = idy + D[0] * k
        jdx2 = jdx + D[1] * k
        if dessert_cafe[idy2][jdx2] not in copied_temp:
            copied_temp.append(dessert_cafe[idy2][jdx2])
        else:
            return
    len_dessert = len(copied_temp)
    if len_dessert > dessert:
        dessert = len_dessert

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dessert_cafe = []
    for _ in range(N):
        dessert_cafe.append(list(map(int, input().split())))
    dessert = -1

    for i in range(N - 2):
        for j in range(1, N - 1):
            # 여기서부터 시작
            wuha(i, j, [dessert_cafe[i][j]], 0)

    print('#%d %d' %(tc, dessert))