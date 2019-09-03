import sys
sys.stdin = open("6485_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    stop_list = []
    bus_list = []
    for _ in range(N):
        AB = list(map(int, input().split()))
        bus_list.append(AB)
    
    P = int(input())
    for _ in range(P):
        C = int(input())
        stop_list.append([C, 0])
    
    for bus in bus_list:
        for i in range(len(stop_list)):
            if bus[0] <= stop_list[i][0] <= bus[1]:
                stop_list[i][1] += 1
    
    result = []
    for stop in stop_list:
        result.append(stop[1])
    result = ' '.join(map(str, result))
    print("#%d %s" %(tc,result))