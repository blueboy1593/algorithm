dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
tc = 0
from heapq import heappush, heappop

while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    zelda_map = []
    for _ in range(N):
        zelda_map.append(list(map(int, input().split())))
    weight_map = [ [140626] * N for _ in range(N) ]

    start = (zelda_map[0][0], 0, 0)
    queue = [start]
    while queue:
        sample = heappop(queue)

        weight = sample[0]
        y = sample[1]
        x = sample[2]

        if weight_map[y][x] < weight:
            continue
        for k in range(4):
            idy = y + dy[k]
            jdx = x + dx[k]
            if 0 <= idy < N and 0 <= jdx < N:
                original_weight = weight_map[idy][jdx]
                new_weight = weight + zelda_map[idy][jdx]
                if new_weight < original_weight:
                    weight_map[idy][jdx] = new_weight
                    temp = (new_weight, idy, jdx)
                    heappush(queue, temp)


    result = weight_map[N - 1][N - 1]
    print('Problem ' + str(tc) + ': ' + str(result))