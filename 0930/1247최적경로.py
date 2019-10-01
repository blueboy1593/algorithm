import sys
sys.stdin = open("1247_input.txt", "r")
import itertools

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    customer = list(map(int, input().split()))
    a = customer.pop(0)
    b = customer.pop(0)
    company = [a, b]
    a = customer.pop(0)
    b = customer.pop(0)
    jip = [a, b]
    minmin = 99999999
    customer_position = []
    for i in range(len(customer)):
        if not i % 2:
            customer_position.append([customer[i], customer[i + 1]])
    
    route = itertools.permutations(customer_position)
    
    for way in route:
        temp_dis = 0
        temp_dis += abs(way[0][0] - company[0]) + abs(way[0][1] - company[1])
        for i in range(len(way) - 1):
            temp_dis += abs(way[i][0] - way[i+1][0]) + abs(way[i][1] - way[i+1][1])
        temp_dis += abs(way[-1][0] - jip[0]) + abs(way[-1][1] - jip[1])
        if temp_dis < minmin:
            minmin = temp_dis
    
    print("#%d %d" %(tc, minmin))
