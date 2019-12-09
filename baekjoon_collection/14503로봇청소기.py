import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
dirty_room = []
for _ in range(N):
    temp = list(map(int, input().split()))
    dirty_room.append(temp)

D = [(-1,0), (0, 1), (1, 0), (0, -1)]
clean_count = 0

def cleanup(i, j, k):
    global clean_count
    if dirty_room[i][j] == 0:
        dirty_room[i][j] = 2
        clean_count += 1
    for l in range(4):
        direction = k - l - 1
        if direction < 0:
            direction += 4
        idy = i + D[direction][0]
        jdx = j + D[direction][1]
        # 여기서 런타임 에러시 iswall 고려하세요
        if dirty_room[idy][jdx] == 0:
            cleanup(idy, jdx, direction)
            return
    # k = k + 1
    # if k == 4:
    #     k = 0
    d2 = (k + 2) % 4
    cidy = i + D[d2][0]
    cjdx = j + D[d2][1]
    if dirty_room[cidy][cjdx] == 2:
        cleanup(cidy, cjdx, k)
    else:
        return

cleanup(r, c, d)

print(clean_count)