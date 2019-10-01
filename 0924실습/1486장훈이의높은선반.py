import sys
sys.stdin = open("1486_input.txt", "r")

import itertools

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    jicwon = list(map(int, input().split()))
    leng = len(jicwon)
    minmin = 99999999
    for i in range(1, leng + 1):
        iter_list = itertools.combinations(jicwon, i)
        for comb in iter_list:
            som = sum(comb)
            if som >= B and som < minmin:
                minmin = som
    result = minmin - B
    
    print("#%d %d" %(tc,result))
            
                
    
    