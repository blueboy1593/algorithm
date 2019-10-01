import sys
# sys.stdin = open("5207_input.txt", "r")
sys.setrecursionlimit(1000000)

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_num = list(map(int, input().split()))
    M_num = list(map(int, input().split()))
    N_num.sort()
    cnt = 0
    
    def find_inornot(l, r, num):
        global numin
        if numin == True:
            return
        if l == r:
            if N_num[l] == num:
                numin = True
            return
        mid = (l + r)//2
        if N_num[mid] == num:
            numin = True
            return
        elif N_num[mid] < num:
            l = mid + 1
            find_inornot(l, r, num)
        elif N_num[mid] > num:
            r = mid - 1
            find_inornot(l, r, num)

    for num in M_num:
        numin = False
        find_inornot(0, N - 1, num)
        if numin == True:
            cnt += 1
    
    print("#%d %d" %(tc, cnt))