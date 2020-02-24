import sys
sys.stdin = open("파핑파핑지뢰찾기_input.txt", "r")
from pprint import pprint
import time
start = time.time()
from collections import deque

# 인접 8방향 검출해서 지뢰 수 계산. 기존의 4방향보다 많이 해줘야한다.
D = [(1,0), (-1,0), (0,1), (0,-1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
def howmany_mines(i, j):
    mine_cnt = 0
    for k in range(8):
        idy = i + D[k][0]
        jdx = j + D[k][1]
        if 0 <= idy < N and 0 <= jdx < N:
            if mines[idy][jdx] == '*':
                mine_cnt += 1
    if mine_cnt == 0:
        mines[i][j] = 0
    else:
        mines[i][j] = mine_cnt

# queue는 2.39 정도
# stack도 2.38 정도
# deque는 그냥 써봄 시간 똑같음.
# queue 와 stack 모두 사용 가능
def click_zero(i, j):
    visited[i][j] = True
    stack = [(i, j)]
    stack = deque(stack)
    while stack:
        sta = stack.popleft()
        y, x = sta
        for k in range(8):
            idy = y + D[k][0]
            jdx = x + D[k][1]
            if 0 <= idy < N and 0 <= jdx < N:
                if visited[idy][jdx] == False:
                    if mines[idy][jdx] == 0:
                        stack.append((idy, jdx))
                        finded_mines[idy][jdx] = 0
                    else:
                        finded_mines[idy][jdx] = mines[idy][jdx]
                    visited[idy][jdx] = True

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    mines = []
    for _ in range(N):
        temp = list(input())
        mines.append(temp)
    cnt = 0

    # 찾은 지뢰 맵 복제
    finded_mines = [0] * N
    for i in range(N):
        finded_mines[i] = mines[i][:]

    # 모든 지뢰 숫자로 검출
    for i in range(N):
        for j in range(N):
            if mines[i][j] == '.':
                howmany_mines(i, j)

    # stack or queue 쓰면서 0이랑 0 주변 숫자 발각시키기
    visited = [ [False] * N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            if mines[i][j] == 0 and visited[i][j] == False:
                click_zero(i, j)
                # cnt += 1
                # 여기 뭐지 왜 cnt 안해야 답이 나오는거지

    for i in range(N):
        for j in range(N):
            if finded_mines[i][j] == '.':
                cnt += 1
    # print(*mines, sep='\n')
    # print(*finded_mines, sep='\n')
    print("#%d %d" %(tc, cnt))

end = time.time()
print(end - start)