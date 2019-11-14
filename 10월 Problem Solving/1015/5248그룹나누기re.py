from pprint import pprint
import sys
sys.stdin = open("5248_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    wish_list = list(map(int, input().split()))
    wish_arr = [ [0] * (N + 1) for _ in range(N + 1) ]

    for i in range(len(wish_list)):
        if not i % 2:
            wish_arr[wish_list[i]][wish_list[i + 1]] = 1
        if i % 2:
            wish_arr[wish_list[i]][wish_list[i - 1]] = 1

    visited = [0] * (N + 1)

    def BFS(i):
        queue = [i]
        while queue:
            for _ in range(len(queue)):
                a = queue.pop(0)
                visited[a] = 1
                for j in range(1, N + 1):
                    if wish_arr[a][j] == 1 and visited[j] == 0:
                        queue.append(j)


    couple = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            BFS(i)
            couple += 1

    print("#%d %d" %(tc, couple))
