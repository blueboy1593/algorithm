from pprint import pprint
import sys
sys.stdin = open("5249_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    VEW_list = [ [0] * (V + 1) for _ in range(V + 1) ]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        VEW_list[n1][n2] = w
        VEW_list[n2][n1] = w
    # pprint(VEW_list)

    start = 0
    node_stack = [start]
    visited = [False] * (V + 1)
    visited[start] = True
    # visited를 사용했어야... 사용하지 않았으면 답이 없다.
    weighted_value = 0
    while len(node_stack) < V + 1:
        minmin = 99999999
        for node in node_stack:
            for j in range(V + 1):
                if visited[j] == False and VEW_list[node][j] != 0:
                    if VEW_list[node][j] < minmin:
                        minmin = VEW_list[node][j]
                        next_stack = (j, minmin)
        node_stack.append(next_stack[0])
        visited[next_stack[0]] = True
        weighted_value += next_stack[1]

    print("#%d %d" %(tc, weighted_value))