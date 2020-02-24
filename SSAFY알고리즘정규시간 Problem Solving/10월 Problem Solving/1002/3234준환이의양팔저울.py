import sys
sys.stdin = open("3234_input.txt", "r")

def make_per(k):
    if k == N:
        per_list.append(temp_per[:])
    else:
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = True
            temp_per[k] = mass[i] 
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
        scale(k, left + a, right)
        if left >= right + a:
            scale(k, left, right + a)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mass = list(map(int, input().split()))

    left = 0
    right = 0
    cnt = 0
    k = 0

    visited = [ False ] * N
    temp_per = [0] * N
    per_list = []
    make_per(k)
    
    for per in per_list:
        scale(k, left, right)

    print("#%d %d" %(tc, cnt))