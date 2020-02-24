import sys
sys.stdin = open("3234_input.txt", "r")
import math

def make_per(k, left, right):
    global cnt
    if k == N:
        cnt += 1
        return
        
    else:
        # k += 1
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = True
            a = mass[i]
            if left + a >= half and k < N:
                remain = (N - k)
                cnt += math.factorial(remain) * (2 ** remain)
            else:
                make_per(k + 1, left + a, right)
            if left >= right + a:
                make_per(k + 1, left, right + a)
            visited[i] = False

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
    make_per(k, left, right)
    
    print("#%d %d" %(tc, cnt))