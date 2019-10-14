import sys
sys.stdin = open("5174_input.txt", "r")
from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    parentchildren = list(map(int, input().split()))
    cnt = 0

    def find_family(node):
        global cnt
        cnt += 1
        for i in range(2):
            if family_list[i][node] != 0:
                find_family(family_list[i][node])

    family_list = [ [0] * (E + 2) for _ in range(2) ]
    
    for i in range(len(parentchildren)):
        if i%2 == 0:
            for j in range(2):
                if family_list[j][parentchildren[i]] == 0:
                    family_list[j][parentchildren[i]] = parentchildren[i + 1]
                    break
    
    find_family(N)
    print("#%d %d" %(tc, cnt))