import sys
sys.stdin = open("5247_input.txt", "r")
from collections import deque
import time
st = time.time()

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * (1000001)

    def bumwi(num):
        if 0 < num <= 1000000:
            return True

    def BFS_DP():
        global cnt
        queue = deque()
        queue.append(N)
        visited[N] = 1
        while queue and visited[M] == 0:
            cnt += 1
            for _ in range(len(queue)):
                i = queue.popleft()
                new_1 = i + 1
                new_2 = i - 1
                new_3 = i * 2
                new_4 = i - 10
                if bumwi(new_1) and visited[new_1] == 0:
                    queue.append(new_1)
                    visited[new_1] = 1
                if bumwi(new_2) and visited[new_2] == 0:
                    queue.append(new_2)
                    visited[new_2] = 1
                if bumwi(new_3) and visited[new_3] == 0:
                    queue.append(new_3)
                    visited[new_3] = 1
                if bumwi(new_4) and visited[new_4] == 0:
                    queue.append(new_4)
                    visited[new_4] = 1
    cnt = 0
    BFS_DP()

    print("#%d %d" %(tc, cnt))
print(time.time() - st)