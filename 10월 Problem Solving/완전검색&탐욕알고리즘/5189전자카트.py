import sys
sys.stdin = open("5189_input.txt", "r")

T = int(input())

def permu(k, i, empty):
    if k == N - 2:
        temtem = [1] + empty + [1]
        route_list.append(temtem)
    else:
        for j in range(N - 1):
            if visited[j] == 0:
                visited[j] = 1
                empty.append(initial_list[j])
                permu(k + 1, j, empty)
                empty.pop()
                visited[j] = 0

for tc in range(1, T + 1):
    N = int(input())
    cartbear = [0] * N
    for i in range(N):
        cartbear[i] = list(map(int, input().split()))
    initial_list = list(range(2, N + 1))
    route_list = []
    minmin = 99999999
    
    for i in range(N - 1):
        empty = [initial_list[i]]
        visited = [0] * N
        visited[i] = 1
        permu(0, i, empty)
    
    for route in route_list:
        case_value = 0
        for k in range(len(route) - 1):
            case_value += cartbear[route[k] - 1][route[k + 1] - 1]
        if case_value < minmin:
            minmin = case_value
    
    print("#%d %d" %(tc, minmin))