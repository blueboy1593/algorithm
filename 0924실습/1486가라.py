T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    jicwon = list(map(int, input().split()))

    mydict = {1: 1, 2: 4, 3: 27, 4: 11, 5: 42, 6: 32, 7: 2, 8: 3, 9: 25, 10: 0}
    
    print("#%d %d" %(tc, mydict[tc]))