import sys
sys.stdin = open("1953_input.txt", "r")
from pprint import pprint

i_list = [1, 0, 3, 2]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
list1 = [1, 1, 1, 1]
list2 = [1, 1, 0, 0]
list3 = [0, 0, 1, 1]
list4 = [1, 0, 0, 1]
list5 = [0, 1, 0, 1]
list6 = [0, 1, 1 ,0]
list7 = [1, 0, 1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    jiha_map = [ list(map(int, input().split())) for _ in range(N) ]
    pprint(jiha_map)
    for i in range(N):
        for j in range(M):
            temp = jiha_map[i][j]
            if temp == 0:
                continue
            if temp == 1:
                jiha_map[i][j] = list1
            if temp == 2:
                jiha_map[i][j] = list2
            if temp == 3:
                jiha_map[i][j] = list3
            if temp == 4:
                jiha_map[i][j] = list4
            if temp == 5:
                jiha_map[i][j] = list5
            if temp == 6:
                jiha_map[i][j] = list6
            if temp == 7:
                jiha_map[i][j] = list7
    visited = [ [False] * M for _ in range(N) ]
    start = [R, C]
    queue = [start]
    cnt = 0
    while queue or cnt < L:
        cnt += 1
        for _ in range(queue):
            a = queue.pop(0)
            y = a[0]
            x = a[1]
            for i in range(4):
