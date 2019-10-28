from pprint import pprint
import sys
sys.stdin = open("5250_input.txt", "r")



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    region_height = [0] * N
    for i in range(N):
        region_height[i] = list(map(int, input().split()))

    near_list =

    def daikstra(i, j):








    visited = [ [False] * N for _ in range(N) ]


    start = (0, 0)
    visited[0][0] = True
    minmin = 99999999

    backtraking(0, 0, 0)
    print("#%d %d" %(tc, minmin))