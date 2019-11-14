import sys
sys.stdin = open("벽돌깨기_input.txt", "r")
from pprint import pprint
from collections import deque

def permu_making(permu, cnt):
    if cnt == N:
        permu_list.append(permu[:])
        return
    cnt += 1
    for i in range(W):
        permu.append(i)
        permu_making(permu, cnt)
        permu.pop()

D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# 2번 터뜨리기 함수
def burst(i, j):
    queue = [(i, j)]
    queue = deque(queue)
    while queue:
        que = queue.popleft()
        y, x = que
        if copied_brick_map[y][x] == 1:
            copied_brick_map[y][x] = 0
        elif copied_brick_map[y][x] >= 2:
            dis = copied_brick_map[y][x]
            copied_brick_map[y][x] = 0
            for k in range(4):
                for d in range(1, dis):
                    idy = y + d * D[k][0]
                    jdx = x + d * D[k][1]
                    if 0 <= idy < H and 0 <= jdx < W:
                        if copied_brick_map[idy][jdx] == 1:
                            copied_brick_map[idy][jdx] = 0
                        elif copied_brick_map[idy][jdx] >= 2:
                            queue.append((idy, jdx))


def go_down():
    for j in range(W):
        stack = []
        for i in range(H):
            if copied_brick_map[i][j] != 0:
                stack.append(copied_brick_map[i][j])
                copied_brick_map[i][j] = 0
        # 앞에서 나온 i를 그대로 갖다가 쓰는 것.
        while stack:
            brick = stack.pop()
            copied_brick_map[i][j] = brick
            i -= 1


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    brick_map = []
    for _ in range(H):
        brick_map.append(list(map(int, input().split())))
    visited = [False] * W
    min_brick = 99999999

    # 1번 순열 그냥 만들어보기
    permu_list = []
    permu_making([], 0)

    # 2번 터뜨리기 시작
    per_length = len(permu_list[0])
    for permu in permu_list:
        # 순열 하나마다 복사 해줘야함
        copied_brick_map = [0] * H
        for i in range(H):
            copied_brick_map[i] = brick_map[i][:]
        # print(permu)
        for p in range(per_length):
            j = permu[p]
            for i in range(H):
                if copied_brick_map[i][j] != 0:
                    burst(i, j)
                    # if permu == [2, 2, 6]:
                    #     pprint(copied_brick_map)
                    break
            # 여기서 이제 3번 내려오게 하기 시작. 가지치기 가능.
            # 여러가지 방법이 있을거같은데 스택이나 큐로 해봐야겠다.
            go_down()
            # if permu == [2, 2, 6]:
            #     pprint(copied_brick_map)

        # 하나의 순열에 대해서 모든 작업이 끝나면 이제 카운트
        cnt = 0
        for i in range(H):
            for j in range(W):
                if copied_brick_map[i][j] != 0:
                    cnt += 1
        if cnt < min_brick:
            min_brick = cnt
        if min_brick == 0:
            break

    print('#%d %d' %(tc, min_brick))