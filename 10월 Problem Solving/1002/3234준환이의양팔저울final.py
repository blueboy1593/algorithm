import sys
sys.stdin = open("3234_input.txt", "r")


def make_per(k):
    if k == N:
        scale(0, 0, 0)
        
    else:
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = True
            per[k] = mass[i] 
            make_per(k + 1)
            visited[i] = False

def scale(k, left, right):
    global cnt
    if k == N:
        cnt += 1
        return
    else:
        a = per[k]
        k += 1
        if left + a >= half and k < N:
            remain = (N - k)
            cnt += (2 ** remain)
        else:
            scale(k, left + a, right)
        if left >= right + a:
            if left >= half and k < N:
                remain = (N - k)
                cnt += (2 ** remain)
                return
            scale(k, left, right + a)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mass = list(map(int, input().split()))
    mass_sum = sum(mass)
    if mass_sum % 2 == 0:
        half = mass_sum // 2
    else:
        half = mass_sum // 2 + 1

    left = 0
    right = 0
    cnt = 0
    k = 0

    visited = [ False ] * N
    per = [0] * N
    make_per(k)
    
    print("#%d %d" %(tc, cnt))